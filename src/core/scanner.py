import os
import socket

from scapy.layers.inet import IP, ICMP
from scapy.layers.l2 import Ether
from scapy.sendrecv import srp1

from config.ports import NORMAL_PORT, FULL_PORT, ENTERPRISE_PORT, NORMAL_1_PORT
from core.structures import IPAddress, Service
from config.config import all_ipaddress, BANNER, WEBCAM_DAHUA
from concurrent.futures import ThreadPoolExecutor, wait, as_completed
import json
import random
import re
import nmap
import socket
import urllib3
import requests
from bs4 import BeautifulSoup

from config.config import key_words, WEBCAM_HIKVISION
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
user_agent = ["Mozilla/5.0 (Linux x86_64; rv:96.0) Gecko/20100101 Firefox/96.0","Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:57.0) Gecko/20100101 Firefox/57.0","Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:58.0) Gecko/20100101 Firefox/58.0","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36","Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:57.0) Gecko/20100101 Firefox/57.0","Mozilla/5.0 (Macintosh; Intel Mac OS X 12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.69","Mozilla/5.0 (Macintosh; Intel Mac OS X 12_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Safari/605.1.15","Mozilla/5.0 (Macintosh; Intel Mac OS X 12.1; rv:96.0) Gecko/20100101 Firefox/96.0","Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.69","Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0","Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36","Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0","Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:96.0) Gecko/20100101 Firefox/96.0","Mozilla/5.0 (X11; Linux i686; rv:96.0) Gecko/20100101 Firefox/96.0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/63.0.3239.84 Chrome/63.0.3239.84 Safari/537.36","Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:91.0) Gecko/20100101 Firefox/91.0","Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0","Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:96.0) Gecko/20100101 Firefox/96.0"]

# 读取JSON文件
with open('./db/service.json', 'r') as file:
    json_data = json.load(file)

# 扫蜜罐
def scan_honey(ip):
    return

# 扫描SSH指纹
def scan_ssh_service_thump(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        s.connect((host, port))
        request = "1".format(host).encode()
        s.sendall(request)
        data = s.recv(1024)
        s.close()
        return parse_ssh_thump(data)
    except:
        pass
# 匹配小点点
def parse_dot(string1):
    pattern = r"(?i)([A-Za-z]+)/([\d.]+)"
    matches = re.match(pattern, string1)
    return str(matches.group(1)) + "/" + str(matches.group(2))
# 匹配SSH
def parse_ssh_thump(string1):
    apps = []
    for i in range(len(json_data)):
        matches_lens = re.findall(json_data[i]['ssh'].encode(), string1)
        matches = re.search(json_data[i]['ssh'].encode(), string1)
        if matches != None:
            for i in range(len(matches_lens[0])):
                if i == 1:
                    app_name = parse_dot("openssh/" + matches_lens[0][i].decode())
                    apps.append(app_name)
                    return (apps)
                if i == 2 and "ubuntu" in str(string1.decode().lower()):
                    app_name = parse_dot("ubuntu/" + matches_lens[0][i].decode())
                    apps.append(app_name)
                    return (apps)
                if i == 2 and "debian" in str(string1.decode().lower()):
                    app_name = parse_dot("debian/" + matches_lens[0][i].decode())
                    apps.append(app_name)
                    return (apps)
def scan_devices(ip):
    devices_name = []
    url = 'http://' + str(ip)
    headers = {
        "User-Agent": random.choice(user_agent)
    }
    proxies = {
        'http':'',
        'https':''
    }
    # 判断大华摄像头
    res = requests.get(url=url + "/webVersion.js", headers=headers, proxies=proxies)
    if "VERSION_GUI" in res.content.decode():
        devices_name.append(WEBCAM_DAHUA)
    # 判断海康摄像头
    elif "dnvrs-webs" in res.headers['Server'].lower():
        devices_name.append(WEBCAM_HIKVISION)
    else:
        devices_name = None
    return devices_name


# 扫描HTTP指纹（单一）
def scan_http(ip):
    headers = {
        "User-Agent": random.choice(user_agent)
    }
    proxies = {
        'http':'',
        'https':''
    }
    paths = [
        "",
        "/html/previewindex.htm",
        "/xmlrpc.php"
    ]
    # 扫描 http 服务
    service_apps = []
    url = 'http://' + str(ip)
    # 判断Wordpress
    res = requests.get(url=url+"/webVersion.js", headers=headers, proxies=proxies)
    soup = BeautifulSoup(res.content, 'html.parser')
    meta_tag = soup.find('meta', {'name': 'generator'})
    if meta_tag:
        content = meta_tag['content']
        service_apps.append(content.replace(" ", "/").lower())
    # 判断大华摄像头
    res = requests.get(url=url + "/webVersion.js", headers=headers, proxies=proxies)
    if "VERSION_GUI" in res.content.decode():
        service_apps.append("dahua/N")
    serv_app = res.headers["Server"].lower()
    serv_app1 = serv_app.split(" ")
    if len(serv_app1) != 1:
        for thump in serv_app1:
            if "centos" in thump:
                service_apps.append("centos/N")
            elif "ubuntu" in thump:
                service_apps.append("ubuntu/N")
            elif "debian" in thump:
                service_apps.append("debian/N")
            service_apps.append(parse_http_thump(thump))
    else:
        service_apps.append(serv_app)
    return service_apps
# 扫描 https 服务
def scan_https(ip):
    headers = {
        "User-Agent": random.choice(user_agent)
    }
    proxies = {
        'http':'',
        'https':''
    }
    paths = [
        "",
        "/html/previewindex.htm",
        "/xmlrpc.php"
    ]
    # 扫描 https 服务
    service_apps = []
    url = 'https://' + str(ip)
    # 判断Wordpress
    res = requests.get(url=url+"/webVersion.js", verify=False, headers=headers, proxies=proxies)
    soup = BeautifulSoup(res.content, 'html.parser')
    meta_tag = soup.find('meta', {'name': 'generator'})
    if meta_tag:
        content = meta_tag['content']
        service_apps.append(content.replace(" ", "/").lower())
    # 判断大华摄像头
    res = requests.get(url=url + "/webVersion.js", verify=False, headers=headers, proxies=proxies)
    if "VERSION_GUI" in res.content.decode():
        service_apps.append("dahua/N")
    serv_app = res.headers["Server"].lower()
    serv_app1 = serv_app.split(" ")
    if len(serv_app1) != 1:
        for thump in serv_app1:
            if "centos" in thump:
                service_apps.append("centos/N")
            elif "ubuntu" in thump:
                service_apps.append("ubuntu/N")
            elif "debian" in thump:
                service_apps.append("debian/N")
            service_apps.append(parse_http_thump(thump))
    else:
        service_apps.append(serv_app)
    return service_apps
# 处理HTTP指纹格式
def parse_http_thump(tthu):
    # pattern = r"(?i)([A-Za-z]+)/(\d+\.\d+(\.\d+)?)"
    pattern = r"(?i)([A-Za-z]+)/([\d.]+)"
    matches = re.match(pattern, tthu)
    if matches:
        server_name = matches.group(1).lower()
        server_version = matches.group(2)
    else:
        if "centos" in tthu:
            return None
        elif "ubuntu" in tthu:
            return None
        elif "debian" in tthu:
            return None
    return f"{server_name}/{server_version}"
# 扫描端口服务
def scan_service_app(ip, port):
    app_version = []
    temp_version = ""
    try:
        nm = nmap.PortScanner()
        # 扫描指定主机的指定端口
        nm.scan(str(ip), str(port))
        # 获取服务版本信息
        if nm[ip].has_tcp(port):
            servicees = nm[ip]['tcp'][port]
            if 'product' in servicees:
                temp_version = f"{servicees['product']}"
                if temp_version == "":
                    return None
                if servicees == "":
                    return None
                elif 'version' in servicees and servicees['version'] != "":
                    temp_version += "/" + (f"{servicees['version']}")
            app_version.append(temp_version)
        return app_version
    except:
        pass
# 单一扫描实现，单一服务
def scan_service(ip, port):
    # 连接 Socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置超时时间为2秒
    sock.settimeout(2)
    # 尝试连接到指定的IP地址和端口号
    result = sock.connect_ex((ip, port))
    app = None
    if result == 0:
        # 获取服务类型
        try:
            service = socket.getservbyport(port)
            request = "GET / HTTP/1.1\r\nHost: {}\r\n\r\n".format(ip)
            sock.send(request.encode())
            response = sock.recv(1024)
            if response.startswith(b"HTTP"):
                thumps = scan_http(ip)
                app = Service(
                    port=port,
                    protocol="http",
                    service_app=thumps
                )
                sock.close()
                return app
            if service == "https":
                thumps = scan_https(ip)
                app = Service(
                    port=port,
                    protocol=service,
                    service_app=thumps
                )
                sock.close()
                return app
            elif service == "ssh":
                app = Service(
                    port=port,
                    protocol=service,
                    service_app=scan_ssh_service_thump(ip, port)
                )
                sock.close()
                return app
            else:
                app = Service(
                    port=port,
                    protocol=service,
                    service_app=scan_service_app(ip, port)
                )
                sock.close()
                return app
        except:
            pass
    return app

# 检查主机是否存活
def Scanner(ip):
    packet = Ether() / IP(dst=ip) / ICMP(type=8) / b'Hello'
    # 发送 ICMP 请求并等待回复
    reply = srp1(packet, timeout=2, verbose=False)
    # 如果 ICMP 相应，
    if reply is not None:
            services = []
            with ThreadPoolExecutor() as executor:
                # 提交任务给线程池
                futures = [executor.submit(scan_service, ip, port) for port in NORMAL_1_PORT]
                # 获取任务的返回结果
                for future in as_completed(futures):
                    result = future.result()
                    if result != None:
                        services.append(result)
                # for port in NORMAL_1_PORT:
                #     result = scan_service(ip, port)
                #     if result != None:
                #         services.append(result)
            if len(services) == 0:
                services = None

            ipAddress = IPAddress(
                deviceinfo=scan_devices(ip),
                honeypot=scan_honey(ip),
                services=services
            )
            all_ipaddress[ip] = ipAddress
