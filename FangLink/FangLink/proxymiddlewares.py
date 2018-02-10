import random
import base64


class ProxyMiddleware(object):
    proxyList = [
        '175.11.51.142:8118',
    ]

    def process_request(self, request, spider):
        # Set the location of the proxy
        pro_adr = random.choice(self.proxyList)
        print("USE PROXY -> %s" % pro_adr)
        request.meta['proxy'] = "http://" + pro_adr