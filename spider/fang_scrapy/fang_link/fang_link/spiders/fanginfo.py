# -*- coding: utf-8 -*-
import scrapy
import re
import logging

# 根据行政区列表爬取对应行政区所有成交房源


class FangInfoSpider(scrapy.Spider):
    name = "fanginfo"
    xinfang_list_url = "http://newhouse.wuhan.fang.com/house/s/"
    district_list = [
        # 东湖高新，洪山，江岸，
        # 东西湖，汉阳，武昌，江汉，经济开发，硚口，黄陂，江夏，青山，蔡甸，新洲，汉南，其他
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
        # for district in self.district_list:
        #     url = self.xinfang_list_url + district + "/b91/"
        url = 'http://newhouse.wuhan.fang.com/house/s/donghugaoxin1/b91/'
        yield scrapy.Request(url=url, callback=self.parse_xinfang_list)

    def parse_xinfang_list(self, response):
        req = response.request
        req.meta["change_proxy"] = True
        curPage = re.search(
            "<span class=\"ff3333\">&nbsp;(.*?)</span>/(.*?)&nbsp;",
            response.text, re.S).group(1)

        totalPage = re.search(
            "<span class=\"ff3333\">&nbsp;(.*?)</span>/(.*?)&nbsp;",
            response.text, re.S).group(2)

        house_content_ul = response.css('div.nl_con  ul li')

        for house_li in house_content_ul:
            # 列表页 楼盘名称 光谷万科中心
            name = house_li.css('div.nlcd_name a::text').extract_first()
            # 地址信息 光谷万科中心标准写字楼均价18000元/平方米
            # price_desc = house_li.css('div.house_type a::text').extract_first()
            if name is not None:
                adname = name.strip()
            # if price_desc is not None:
            #     ad_price_desc = price_desc.strip()
            yield {'name': adname}
            # yield scrapy.Request(
            #     url=house_url, callback=self.parse_xinfang_data)

        if curPage != totalPage:
            next_page = int(curPage) + 1
            yield scrapy.Request(
                url=response.url.split('b9')[0] + 'b9' + str(next_page) + '/',
                callback=self.parse_xinfang_list)

    def parse_xinfang_data(self, response):
        yield {'name': response.url}
