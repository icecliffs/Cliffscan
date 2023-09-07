# -*- encoding=utf-8 -*-
import click
import json
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from config.config import all_ipaddress, THREADS, BANNER
from controller.controller import Controller
from core.structures import IPAddressEncoder
import concurrent.futures




# 检查环境是否支持
if sys.version_info < (3, 7):
    sys.stdout.write("Sorry, CliffScan requires Python 3.7 or higher\n")
    sys.exit(1)




def process_ip(ip):
    Controller(ip)

if __name__ == '__main__':
    # 测试扫描
    # 记录程序开始时间
    start_time = time.time()
    # 扫描单个
    # test_ip = ["113.30.191.68"]
    # all_ip = ["211.22.90.0/24", "198.175.7.0/24", "64.154.25.0/24", "43.135.46.0/24", "35.206.251.0/24",
    #            "185.241.5.0/24", "165.22.92.0/24", "113.30.150.0/24", "206.189.61.0/24", "24.199.98.0/24",
    #            "164.92.167.0/24", "170.64.148.0/24", "165.22.22.0/24", "104.248.48.0/24", "165.22.17.0/24",
    #            "170.64.158.0/24", "113.30.191.0/24", "113.30.151.0/24", "45.83.43.0/24", "185.139.228.0/24",
    #            "103.252.118.0/24", "185.229.226.0/24", "103.252.119.0/24", "159.65.5.0/24", "134.122.18.0/24",
    #            "142.93.224.0/24", "68.183.177.0/24", "81.28.6.0/24", "142.93.206.0/24", "143.110.240.0/24",
    #            "143.110.244.0/24", "68.183.233.0/24", "138.68.173.0/24", "68.183.46.0/24", "134.122.46.0/24",
    #            "134.209.202.0/24", "64.226.68.0/24", "159.65.92.0/24", "137.184.166.0/24", "83.229.87.0/24"]
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(process_ip, ip) for ip in all_ip]
        for future in concurrent.futures.as_completed(futures):
            try:
                result = future.result()
                # 处理每个任务的结果
                # result = future.result() 为 Controller(ip) 的返回结果
                print("Task completed successfully.")
            except Exception as e:
                print("Task encountered an error:", str(e))
    json_data = json.dumps(all_ipaddress, cls=IPAddressEncoder)
    result = open("result.json", "wb")
    result.write(json_data.encode('utf-8'))
    result.close()
    # 记录程序结束时间
    end_time = time.time()
    # 计算程序运行时间
    duration = end_time - start_time
    # 转换为时、分、秒格式
    hours = int(duration / 3600)
    minutes = int((duration % 3600) / 60)
    seconds = int(duration % 60)
    # 打印程序运行时间
    print(f"程序运行时间：{hours}小时 {minutes}分钟 {seconds}秒")