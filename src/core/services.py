import socket
from concurrent.futures import ThreadPoolExecutor, wait, as_completed

class Scanner:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def scan_port(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2)
            s.connect((self.ip, self.port))
            request = f"Cliffscan\r\n".format(self.ip).encode()
            s.sendall(request)
            data = s.recv(1024)
            s.close()
            print("[*] {0} - {1}".format(self.port, data))
        except IOError as e:
            print(e)

    def scan_hosts(self):
        

class Parser:
    def __init__(self, parse_str):
        self.parse_str = parse_str
    # RFC 4251
    def ssh_parse(self):
        return




ip = "192.168.233.234"
test_ports = [
    20,
    21,
    22,
    80,
    443,
    888,
    3300,
    3306,
    9200,
    10000,
    10002,
    10003,
    10004,
    10010,
    12345,
]
ports = [port for port in range(80, 3000)]
with ThreadPoolExecutor() as executor:
    try:
        futures = [executor.submit(Scanner(ip, port).scan_port()) for port in test_ports]
        for future in as_completed(futures):
            result = future.result()
            print(result)
    except IOError as e:
        print(e)

# -*- coding: utf-8 -*-
# port_scan.py <host> <start_port>-<end_port>
# import sys
# from socket import *
# host = sys.argv[1]
# portstrs = sys.argv[2].split('-')
# start_port = int(portstrs[0])
# end_port = int(portstrs[1])
# target_ip = gethostbyname(host)
# opened_ports = []
# for port in range(start_port, end_port):
#     str_info = 'Port %d...' % port
#     sock = socket(AF_INET, SOCK_STREAM)
#     sock.settimeout(10)
#     result = sock.connect_ex((target_ip, port))
#     if result == 0:
#         opened_ports.append(port)
#         str_info += 'OPEN'
#         print(str_info)
# print("Opened ports:")
# for i in opened_ports:
#     print(i)
