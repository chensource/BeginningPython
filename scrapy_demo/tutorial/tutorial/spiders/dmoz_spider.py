import scrapy
import re


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    xinfang_list_url = "http://newhouse.wuhan.fang.com/house/s/"
    district_list = [
        #东湖高新，洪山，江岸，东西湖，汉阳，武昌，江汉，经济开发，硚口，黄陂，江夏，青山，蔡甸，新洲，汉南，其他
        'donghugaoxin1',
        'honshan1',
        'jiangan1',
        'dongxihu1',
        'hanyang1',
        'wuchang1',
        'jianghan1',
        'jingjikaifaqu'
        'hanyang',
        'qiaokou2',
        'huangpi2',
        'jiangxia2',
        'qingshan2',
        'caidian2',
        'xinzhou2',
        'hannan2',
        'qita1'
    ]

    def start_requests(self):
        for district in self.district_list:
            url = self.xinfang_list_url + district + "/b91/"
            yield scrapy.Request(url=url, callback=self.parse_xinfang_list)

    def parse_xinfang_list(self, response):
        curPage = re.search(
            "<span class=\"ff3333\">&nbsp;(.*?)</span>/(.*?)&nbsp;",
            response.text, re.S).group(1)

        totalPage = re.search(
            "<span class=\"ff3333\">&nbsp;(.*?)</span>/(.*?)&nbsp;",
            response.text, re.S).group(2)

        house_url_list = response.css('div.nlc_img a::attr(href)').extract()

        for house_url in house_url_list:
            yield scrapy.Request(
                url=house_url, callback=self.parse_xinfang_data)

        if curPage != totalPage:
            next_page = int(curPage) + 1
            yield scrapy.Request(
                url=response.url.split('b9')[0] + 'b9' + str(next_page) + '/',
                callback=self.parse_xinfang_list)

    def parse_xinfang_data(self, response):
        yield {'name': response.url}
