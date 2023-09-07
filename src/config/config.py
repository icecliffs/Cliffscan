# 全局配置文件
# 作者
__author__ = "rYu1nser"
# 版本号
__version__ = "0.0.9"
options = {
    # URL备用
    "urls": [],
    # 默认配置文件为空
    "config": None,
    # 多线程默认数量
    "thread_count": 25,
}
# 线程数
THREADS = 25
# 存储IP地址
all_ipaddress = {}
# 全局存储服务
# BANNER
BANNER = f"""
   ___ _ _  __  __ __                 
  / __\ (_)/ _|/ _/ _\ ___ __ _ _ __  
 / /  | | | |_| |_\ \ / __/ _` | '_ \       v{__version__}
/ /___| | |  _|  _|\ \ (_| (_| | | | |      @{__author__}
\____/|_|_|_| |_| \__/\___\__,_|_| |_|
"""
# 摄像头
WEBCAM = "webcam"
# 摄像头::海康威视
WEBCAM_HIKVISION = "webcam/hikvision"
# 摄像头::大华
WEBCAM_DAHUA = "webcam/dahua"
# 路由器
ROUTER = "router"
# 网关
GATEWAY = "gateway"
# 虚拟专用网络
VPN = "vpn"
# 存储设备
STORAGE = "storage"
# 交换机
SWITCH = "switch"
# 打印机设备
PRINTERS = "printers"
# 代理服务器
PROXY_SERVER = "proxy server"
# 虚拟化平台
KVM = "kvm"
# 内容分发平台
CDN = "cdn"
# 移动通信
PHONE = "phone"
# 虚拟网络设备
BRIDGE = "bridge"
# 安全防护设备
SECURITY = "security"
# 关键词
key_words = {
    "rabbitmq/N":"rabbitmq"
}