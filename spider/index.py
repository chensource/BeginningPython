#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv
from pyquery import PyQuery as pq
import time

import sys

reload(sys)
sys.setdefaultencoding('utf8')

# import resource


def getLink(i):
    url = "http://wh.fang.lianjia.com/loupan/pg{0}/".format(i)
    return url


# def getFacilities(link):
#     "return facility links on that page"
#     facility_links = []
#     # base_url = "http://www.39yanglao.com/"
#     soup = getSoup(link)
#     print(soup)
#     table_ul = soup.find("ul", {"id": "UL_List", "class": "findUl"})
#     table_li = table_ul.findAll("li")
#     for name in table_li:
#         link2 = name.find("a")["href"]
#         link2 = base_url + link2
#         facility_links.append(link2)
#     return facility_links


# def getSoup(url):
#     "Return parsed html"
#     response = requests.get(url)
#     sc = response.status_code
#     if sc != 200:
#         print("Error getting URL: %s" % sc)
#         return -1
#     content = open(response.content, "w", encoding='utf-8')
#     soup = BeautifulSoup(content, "lxml")
#     return soup


# def getJson(url):
#     response = requests.get(url)
#     sc = response.status_code
#     if sc != 200:
#         print("Error getting URL: %s" % sc)
#         return -1
#     jsonValue = json.loads(response.content)
#     return jsonValue


# def getInfo(s):
#     info_s = print(h1.get_text())
#     print(info_s)
#     # name = info_s.find("h2").find("a").text()
#     # return [name]

facility_list = []
for i in range(70, 71):
    # print "getting links on page {0}".format(i)
    link = getLink(i)
    # print(link)
    # t = getFacilities(link)
    facility_list.append(link)
    # print(link)

# with open("links.csv", "rb") as f:
#     w = csv.writer(f)
#     w.writerow(facility_list)

# datareader = csv.reader(open("links.csv", "rb"), delimiter=",")
# for row in datareader:
#     facility_list.extend(row)


data = []
for l in facility_list:
    print(l)
    # print l
    if l == -1:
        continue
    # html = urllib.request.urlopen("http://www.baidu.com").read()
    # response = open(html, "w", encoding='utf-8')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36',
        "Upgrade-Insecure-Requests": "1",
        "Referer": "http://wh.fang.lianjia.com/loupan/",
        "Host": "wh.fang.lianjia.com",
        "Cookie": "lianjia_uuid=bea0499d-965d-47d6-9f2f-ee8e342ecd67; select_city=420100; logger_session=564ea02379eae4cdc50e990ed27dcd57; UM_distinctid=15e0cd9856194d-06feb0b8289366-c313760-15f900-15e0cd98562d56; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1503456471; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1503456471; _smt_uid=599cecd7.15f5ec94; CNZZDATA1256296306=956016100-1503454205-%7C1503454205; _ga=GA1.2.1931129264.1503454155; _gid=GA1.2.713401299.1503454155; CNZZDATA1254525948=36830779-1503449171-%7C1503454571; CNZZDATA1255633284=329318859-1503449371-%7C1503455287; CNZZDATA1255604082=1228253119-1503451868-%7C1503451868; lianjia_ssid=e585f8af-1be1-46d9-993a-adcde85ec060",
        "Connection": "keep-alive",
        "Cache-Control": "max-age=0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate"
    }
    doc = pq(l, headers=headers)
    rs = doc.html().encode("utf-8")
    iss = pq(rs).find(".house-lst li .info-panel h2 a").text()
    print(iss)
    for i in iss.split(" "):
        data.append([i])
    time.sleep(2)

with open("data.csv", "w") as f:
    w = csv.writer(f)
    for d in data:
        w.writerow([item for item in d])
