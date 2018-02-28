import random
import base64
from scrapy import log
import logging

import requests


class ProxyMiddleware(object):
    def get_proxys(self):
        return requests.get("http://127.0.0.1:5010/get_all/").json()

    def delete_proxy(self, proxy):
        requests.get("http://127.0.0.1:5010/delete/?proxy={}".format(proxy))

    def verify_one_proxy(self, old_queue, new_queue):
        while 1:
            proxy = old_queue.get()
            if proxy == 0:
                break
            protocol = 'https' if 'https' in proxy else 'http'
            proxies = {protocol: proxy}
            try:
                if requests.get('http://www.baidu.com', proxies=proxies, timeout=2).status_code == 200:
                    new_queue.put(proxy)
            except:
                print('fail %s' % proxy)

    def process_request(self, request, spider):
        proxys = self.get_proxys()
        proxy = random.choice(proxys)
        # Set the location of the proxy
        log.msg('USE PROXY -> ' + proxy, level=logging.DEBUG)
        request.meta['proxy'] = "http://" + proxy
