import datetime
import json
import time
import logging
from config.config import all_ipaddress
from config.result import ERROR
import concurrent.futures
import threading
from tqdm import tqdm
import ipaddress
from core.scanner import Scanner
from core.structures import IPAddressEncoder

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

# 划分子网里的所有IP地址
def cidr_to_ips(cidr):
    try:
        ip, mask = cidr.split('/')
        ip_parts = list(map(int, ip.split('.')))
        mask = int(mask)
        ip_start = ip_parts[0] << 24 | ip_parts[1] << 16 | ip_parts[2] << 8 | ip_parts[3]
        ip_end = ip_start | (2 ** (32 - mask) - 1)
        ip_addresses = []
        for ip_int in range(ip_start, ip_end + 1):
            ip_parts = [(ip_int >> 24) & 255, (ip_int >> 16) & 255, (ip_int >> 8) & 255, ip_int & 255]
            ip_address = '.'.join(map(str, ip_parts))
            ip_addresses.append(ip_address)
        return ip_addresses
    except:
        return exit(ERROR)

# 批量扫描线程
class ScanThread(threading.Thread):
    def __init__(self, ip):
        threading.Thread.__init__(self)
        self.ip = ip
    def run(self):
        Scanner(self.ip)

def Controller(ip):
    ip_list = [str(ip) for ip in ipaddress.IPv4Network(ip)]
    threads = []
    for ip in ip_list:
        thread = ScanThread(ip)
        threads.append(thread)
        thread.start()

    with tqdm(total=len(threads)) as pbar:
        for thread in threads:
            thread.join()
            pbar.update(1)
