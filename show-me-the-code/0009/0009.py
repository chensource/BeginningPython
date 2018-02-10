import re
import urllib.request

def get_context(url):
    html_content = urllib.request.urlopen(url).read()
    r = re.compile('href="(.*?)"')
    result = r.findall(html_content.decode('utf-8'))
    return result


if __name__ == '__main__':
    url = 'http://sh.centanet.com/xiaoqu/'
    print(get_context(url))