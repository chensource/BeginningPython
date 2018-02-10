#-*- coding: UTF-8 -*-

import urllib
from bs4 import BeautifulSoup
import html5lib


def get_context(url):
    html_content = (urllib.request.urlopen(url).read())
    print(html_content.decode('GBK', 'ignore').encode('UTF-8'))
    soup = BeautifulSoup(html_content,"html5lib")
    result = soup.get_text("|", strip=True)
    return result


if __name__ == '__main__':
    url = 'http://sh.centanet.com/xiaoqu/'
    print(get_context(url))
