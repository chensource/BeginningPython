# -*- coding: utf-8 -*-
import scrapy
import re
import logging
from fang_link.items import fang_list_item, fang_detail_item, house_detail_item

# 根据行政区列表爬取对应行政区所有成交房源


class FangInfoSpider(scrapy.Spider):
    name = "fanginfo"
    xinfang_list_url = "http://newhouse.wuhan.fang.com/house/s/"
    district_list = [
        # 东湖高新，洪山，江岸，
        # 东西湖，汉阳，武昌，江汉，经济开发，硚口，黄陂，江夏，青山，蔡甸，新洲，汉南，其他
        'donghugaoxin1',
        'hongshan1',
        'jiangan1',
        'dongxihu1',
        'hanyang1',
        'wuchang1',
        'jianghan1',
        'jingjikaifaqu',
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
        '''
        售房新房列表数据抓取
        '''
        listitem = fang_list_item()
        curPage = re.search(
            "<span class=\"ff3333\">&nbsp;(.*?)</span>/(.*?)&nbsp;",
            response.text, re.S).group(1)

        totalPage = re.search(
            "<span class=\"ff3333\">&nbsp;(.*?)</span>/(.*?)&nbsp;",
            response.text, re.S).group(2)

        house_content_ul = response.css('div.nl_con ul li')

        for house_li in house_content_ul:
            # 楼盘链接  http://guangguzhongxinchengld.fang.com/
            fang_url = house_li.css(
                'div.nlcd_name a::attr(href)').extract_first()
            if fang_url:
                listitem['fang_url'] = fang_url.strip()

            # 楼盘名称 光谷万科中心
            name = house_li.css('div.nlcd_name a::text').extract_first()
            if name:
                listitem['ad_name'] = name.strip()

            # 房源地址信息
            relative_message = house_li.css('div.relative_message')
            if relative_message:
                # 楼盘地址 [二至三环]东湖高新区关山大道与南湖大道交汇处（光谷天地旁）
                listitem['address'] = relative_message.css(
                    'div.address a::attr(title)').extract_first().strip()
                # 区域信息 东湖高新区
                listitem['ad_area'] = relative_message.css(
                    'div.address a span.sngrey::text').extract_first().strip()[1:-1]

            # 房源状态 [在售][住宅][标签]
            fangyuan = house_li.css('div.fangyuan')
            if fangyuan:
                # 销售状态
                listitem['sales_status'] = fangyuan.css(
                    'span::text').extract_first().strip()
                # 房源类型
                listitem['property_category'] = fangyuan.css(
                    'a::text').extract_first().strip()
                # 特色
                listitem['features'] = fangyuan.css(
                    'a::text')[1:-1].re(r'(\w+)')

            # 价格
            listitem['show_price'] = house_li.css(
                'div.nhouse_price span::text').extract_first()

            # 存储list数据
            yield listitem

            if fang_url:
                yield scrapy.Request(
                    url=fang_url, callback=self.parse_xinfang_data)

        # 下一页翻页
        if curPage != totalPage:
            next_page = int(curPage) + 1
            yield scrapy.Request(
                url=response.url.split('b9')[0] + 'b9' + str(next_page) + '/',
                callback=self.parse_xinfang_list)

    def parse_xinfang_data(self, response):
        detail_item = fang_detail_item()
        # 唯一标识
        detail_item['fang_url'] = response.url

        # 导航栏
        head = response.css('div.nav')
        if head:
            # 详细信息url
            house_detail_url = head.css(
                'div.navleft a:contains("详")::attr(href)').extract_first()
            if house_detail_url:
                detail_item['house_detail_url'] = house_detail_url.strip()

            # 动态
            house_info_url = head.css(
                'div.navleft a:contains("动态")::attr(href)').extract_first()
            if house_info_url:
                detail_item['house_info_url'] = house_info_url.strip()

            # 户型
            house_type_url = head.css(
                'div.navleft a:contains("户型")::attr(href)').extract_first()
            if house_type_url:
                detail_item['house_type_url'] = house_type_url.strip()

            # 相册
            house_image_url = head.css(
                'div.navleft a:contains("相册")::attr(href)').extract_first()
            if house_image_url:
                detail_item['house_image_url'] = house_image_url.strip()

            # 价格
            house_price_url = head.css(
                'div.navleft a:contains("价")::attr(href)').extract_first()
            if house_price_url:
                detail_item['house_price_url'] = house_price_url.strip()

        # huxing_dls = response.css('div.huxing div.rn dl')
        # if huxing_dls:
        #     for huxing_dl in huxing_dls:
        #         titles = huxing_dl.css('h2 a::text').re('(\w+)')
        #         detail_item['house_type_name'] = titles[0].strip()
        #         house_room_str = re.findall(
        #             '(\d+)', huxing_dl.css('h2 a::text').re('\w+\s+(\w+)\s+')[0])
        #         if house_room_str and isinstance(house_room_str, list):
        #             detail_item['house_type_room_cnt'] = house_room_str[0]
        #             detail_item['house_type_hall_cnt'] = house_room_str[1]
        #             detail_item['house_type_kitchen_cnt'] = house_room_str[2]
        #             detail_item['house_type_toilet_cnt'] = house_room_str[3]

        #         detail_item['house_type_size'] = titles[2].strip()
        #         detail_item['house_type_desc'] = huxing_dl.css(
        #             'p a::attr(title)').extract_first()
        yield detail_item

        if house_detail_url:
            yield scrapy.Request(
                url=house_detail_url, callback=self.parse_house_detail)

        # if house_info_url:
        #     yield scrapy.Request(
        #         url=house_info_url, callback=self.parse_xinfang_data)

        # if house_type_url:
        #     yield scrapy.Request(
        #         url=house_type_url, callback=self.parse_xinfang_data)

        # if house_image_url:
        #     yield scrapy.Request(
        #         url=house_image_url, callback=self.parse_xinfang_data)
        # print(response.text)
        # yield {'name': response.url}

    def parse_house_detail(self, response):
        '''
            房源详细信息
        '''
        item = house_detail_item()
        #------------------------------ 基本信息 ---------------------------------------- #
        # base_info = response.css('div.main-item h3:contains("基本信息") ~ ul')
        # 物业类别
        house_type = response.css(
            'div.list-left:contains("物业类别") + div.list-right::text').extract_first()

        if house_type:
            item['house_type'] = house_type.strip()
        else:
            item['house_type'] = ''

            # 建筑类别
        building_type = response.css(
            'div.list-left:contains("建筑类别") + div.list-right sapn::text').re('\w+')

        if building_type:
            item['building_type'] = building_type.strip()
        else:
            item['building_type'] = ''

        # 项目特色
        building_features = response.css(
            'div.list-left:contains("项目特色") + div.list-right sapn.tag::text').extract_first()

        if building_features:
            item['building_features'] = building_features.strip()
        else:
            item['building_features'] = ''

        # 装修状况
        decoration = response.css(
            'div.list-left:contains("装修状况") + div.list-right::text').extract_first()

        if decoration:
            item['decoration'] = decoration.strip()
        else:
            item['decoration'] = ''

        # 产权年限
        property_years = response.css(
            'div.list-left:contains("产权年限") + div.list-right p::text')..extract_first()

        if property_years:
            item['property_years'] = property_years.strip()
        else:
            item['property_years'] = ''

        # 环线位置
        loop_location = response.css(
            'div.list-left:contains("环线位置") + div.list-right::text').extract_first()

        if loop_location:
            item['loop_location'] = loop_location.strip()
        else:
            item['loop_location'] = ''

        # 开发商
        developer = response.css(
            'div.list-left:contains("开") + div.list-right-text a::text').extract_first()

        if developer:
            item['developer'] = developer.strip()
        else:
            item['developer'] = ''

        #----------------------------------------END 基本信息 ---------------------------------------- #

        #---------------------------------------- 销售信息 ---------------------------------------- #

        # 销售状态
        sales_status = response.css(
            'div.list-left:contains("销售状态") + div.list-right::text').extract_first()

        if sales_status:
            item['sales_status'] = sales_status.strip()
        else:
            item['sales_status'] = ''

        # 开盘时间
        opening_time = response.css(
            'div.list-left:contains("开盘时间") + div.list-right::text').extract_first()

        if opening_time:
            item['opening_time'] = opening_time.strip()
        else:
            item['opening_time'] = ''

        # 交房时间
        delivery_time = response.css(
            'div.list-left:contains("交房时间") + div.list-right::text').extract_first()

        if delivery_time:
            item['delivery_time'] = delivery_time.strip()
        else:
            item['delivery_time'] = ''

        # 售楼地址
        sales_address = response.css(
            'div.list-left:contains("售楼地址") + div.list-right::text').extract_first()

        if sales_address:
            item['sales_address'] = sales_address.strip()
        else:
            item['sales_address'] = ''

        # 预售许可证

        #---------------------------------------- 销售信息 ---------------------------------------- #

        #---------------------------------------- 周边设施 ---------------------------------------- #

        other_info = response.css('ul.sheshi_zb li::text').extract()
        if other_info:
            # 交通
            traffic = " ".join(other_info[0:3])
            # 学校
            school = other_info[3]
            # 商场
            mall = other_info[4]
            # 医院
            hospital = other_info[5]
            # 银行
            bank = other_info[6]

            if traffic:
                item['traffic'] = traffic.strip()
            else:
                item['traffic'] = ''

            if school:
                item['school'] = school.strip()
            else:
                item['school'] = ''

            if hospital:
                item['hospital'] = hospital.strip()
            else:
                item['hospital'] = ''

            if bank:
                item['bank'] = bank.strip()
            else:
                item['bank'] = ''

        #---------------------------------------- 周边设施 ---------------------------------------- #

        #---------------------------------------- 小区信息 ---------------------------------------- #
        # 占地面积
        land_area = response.css(
            'div.list-left:contains("占地面积") + div.list-right::text').re('(\d+)')

        # 建筑面积
        build_area = response.css(
            'div.list-left:contains("建筑面积") + div.list-right::text').re('(\d+)')

        # 容积率
        volume_rate = response.css(
            'div.list-left:contains("容") + div.list-right::text').re('(\d+(\.\d+)?)')[0]

        # 容积率
        greening_rate = response.css(
            'div.list-left:contains("绿") + div.list-right::text').re('(\d+(\.\d+)?)')[0]

        parking_count = response.css(
            'div.list-left:contains("车") + div.list-right::text').re('(\d+(\.\d+)?)')

        house_count = response.css(
            'div.list-left:contains("户") + div.list-right::text').re('(\d+(\.\d+)?)')

        property_company = response.css(
            'div.list-left:contains("物业公司") + div.list-right a::text').extract()

        # 物业费
        property_costs = response.css(
            'div.list-left:contains("物") + div.list-right::text').re('(\d+(\.\d+)?)')

        # 物业费描述
        property_costs_description = response.css(
            'div.list-left:contains("物业费描述") + div.list-right-floor::text').extract()

        #---------------------------------------- 小区信息 ---------------------------------------- #

        #---------------------------------------- 项目简介 ---------------------------------------- #

        project_description = response.css('p.intro::text').extract_first()

        #---------------------------------------- 项目简介 ---------------------------------------- #

    print(response.url)
