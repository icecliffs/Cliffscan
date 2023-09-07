# Service Object



import json
class Service:
    def __init__(self, port, protocol, service_app):
        self.port = port
        self.protocol = protocol
        self.service_app = service_app
class IPAddress:
    def __init__(self, deviceinfo, honeypot, services):
        self.deviceinfo = deviceinfo
        self.honeypot = honeypot
        self.services = services

class IPAddressEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, IPAddress):
            return {
                "services": obj.services,
                "deviceinfo": obj.deviceinfo,
                "honeypot": obj.honeypot,
            }
        elif isinstance(obj, Service):
            return {
                "port": obj.port,
                "protocol": obj.protocol,
                "service_app": obj.service_app
            }
        return super().default(obj)