import urllib.request
from bs4 import BeautifulSoup
import html5lib
import re
import os


def get_image(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    soup = BeautifulSoup(html, "html5lib")
    imageList = soup.find_all('img', class_="lazy")
    # print(len(imageList))
    dirct = '0013'
    path = os.path.join(os.path.abspath('.'), dirct)
    try:
        if not os.path.exists(dirct):
            os.mkdir(dirct)
    except:
        print('Failed to create directory in %s' % dirct)
        exit()
    for m in imageList:
        img_url = m['data-original']

        print(img_url)
        img_name = m['alt']
        img_content = urllib.request.urlopen(img_url).read()
        # print(img_url)
        file_name = str(img_name) + '.jpg'

        with open(os.path.join(path, file_name), 'wb') as wf:
            wf.write(img_content)
        # downloadImage(img_url,file_name=file_name)
    print('Done  %s!' % url)


def get_urls(url):
    L = []
    page = urllib.request.urlopen(url)
    html = page.read()
    soup = BeautifulSoup(html, 'html5lib')
    urls = soup.find_all('a', class_='fsm')
    lastUrl = urls[1]['href']
    print(lastUrl)
    pattern = re.compile(r'(/\w*/?)(\w)(\d+)/')
    match = pattern.match(lastUrl)
    print(match)
    if match:
        num = match.groups()[2]
        url = url + match.groups()[1]

    for i in range(int(num)):
        link = url + str(i + 1) + '/'
        L.append(link)

    for imageurl in L:
        get_image(imageurl)


if __name__ == '__main__':
    url = 'http://sh.centanet.com/xiaoqu/'
    get_urls(url)
