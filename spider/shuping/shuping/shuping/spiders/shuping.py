# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from shuping.items import YswItem, YswItems
import json
from scrapy import Selector
import re


class ShupingSpider(scrapy.Spider):
    name = 'shuping'
    #allowed_domains = ['www.yousuu.com']
    start_urls = ['http://www.yousuu.com/book/124600']

    # 此方法解析评论第一页的一级书评
    def parse(self, response):
        # 遍历每个一级书评，获得信息
        for r in response.xpath('//*[@id="content"]/div'):
            item = YswItem()
            # 发帖时间
            item['time'] = r.xpath('string(./div/div/div[1]/div/span[2])'
                                   ).extract_first().strip()

            # 获得赞同数
            agree = r.xpath('string(./div/div/div[2]/button[1]/span)'
                            ).extract_first().strip()
            if agree:
                item['agree'] = agree
            else:
                item['agree'] = '0'

            # 一级书评内容
            item['fir_text'] = r.xpath(
                'string(./div/div/p)').extract_first().replace('\r\n',
                                                               '').replace(
                                                                   ' ', '')

            # 二级评论数：
            sec_num = r.xpath('string(./div/div/div[2]/button[2]/span)'
                              ).extract_first().strip()
            if sec_num:
                item['sec_num'] = sec_num

                # 获取二级评论url的组成部分cid
                cid = r.xpath('./@cid').extract_first().strip()

                # 补全二级评论第一页的url
                sec_text_url = "http://www.yousuu.com/ajax/getonecomment?render=true&cid={}".format(
                    cid)

                # 将每一个一级书评下的所有二级书评的获取都交给sp_two.parse
                sec_text_list = []
                yield Request(
                    sec_text_url,
                    meta={'sec_text_list': sec_text_list,
                          'item': item},
                    callback=self.parse_shuping_two)
            else:
                item['sec_num'] = '0'
                yield item
        return print('一级书评第一页!')

    def parse_shuping_two(self, response):
        items = YswItems()
        # json格式转为python结构数据
        jsobj = json.loads(response.body)
        # 从字典中提取html的值，也就是二级评论的html格式文本
        html = jsobj['html']
        # 获得二级书评第一页的所有二级书评内容，放在列表result中，迭代这个parse方法时，依次是第2,3，页等等
        result = Selector(text=html).xpath('//p/text()').extract()
        # 获得上一个Request传递过来的参数, 第一次是一个空列表
        sec_text_list = response.meta['sec_text_list']
        # 获得shuping.parse()传来的item
        item = response.meta['item']
        '''每一页的二级评论内容放在一个列表result中，这个列表又放在列表sec_text_list中
        二级书评每一页的第一个书评都是它的一级书评内容，所以从每一页新的二级书评从第二个算起'''
        sec_text_list.extend(result[1:])

        # 判断二级评论是否还有下一页
        nextpage = Selector(
            text=html).xpath('//a[text()="更多回复"]/@onclick').extract_first()
        if nextpage:
            # 获得下一页的cid
            cid = re.search(r"(.*?)'(.*?)',(.*)", nextpage).group(2)
            # 获取下一页的t
            t = re.search("(.*),(.*?)\)", nextpage).group(2)
            # 组装二级评论下一页的url
            next_page_url = "http://www.yousuu.com/ajax/getcommentreply?cid={}&t={}&render=true".format(
                cid, t)
            # print('next_page_url')
            # 迭代这个方法继续获得下一页的二级评论内容
            yield Request(
                next_page_url,
                meta={'sec_text_list': sec_text_list,
                      'item': item},
                callback=self.parse_shuping_two)
        else:

            items['sec_text'] = sec_text_list
            items['time'] = item['time']
            items['agree'] = item['agree']
            items['sec_num'] = item['sec_num']
            items['fir_text'] = item['fir_text']
            print('已获取此一级书评的全部二级书评！')
            yield items
