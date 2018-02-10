import random
import base64


class ProxyMiddleware(object):
    proxyList = ['221.7.255.168:8080', '47.96.134.8:8123']

    def process_request(self, request, spider):
        # Set the location of the proxy
        pro_adr = random.choice(self.proxyList)
        print("USE PROXY -> %s" % pro_adr)
        request.meta['proxy'] = "http://" + pro_adr