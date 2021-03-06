# -*- coding: utf-8 -*-
import json
import scrapy
import re
import logging
import time
from urllib.parse import quote
import urllib
from fang_link.items import fang_list_item, house_detail_item, house_info_item, house_type_item, house_photo_item, house_price, house_permit

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
        'hannan2'
        #'qita1'  应业务线要求，去掉非武汉市城区的楼盘
    ]

    def start_requests(self):
        for district in self.district_list:
            url = self.xinfang_list_url + district + "/a77-b91/'"
            yield scrapy.Request(url=url, callback=self.parse_xinfang_list)

        # 测试单页数据
        # url = 'http://newhouse.wuhan.fang.com/house/s/donghugaoxin1/a77-b91/'
        # yield scrapy.Request(url=url, callback=self.parse_xinfang_list)

    def parse_xinfang_list(self, response):
        '''
        售房新房列表数据抓取
        '''
        item = fang_list_item()
        item['item_type'] = 'house_list'
        curPage = re.search(
            "<span class=\"ff3333\">&nbsp;(.*?)</span>/(.*?)&nbsp;", response.text, re.S).group(1)

        totalPage = re.search(
            "<span class=\"ff3333\">&nbsp;(.*?)</span>/(.*?)&nbsp;", response.text, re.S).group(2)

        house_content_ul = response.xpath(
            '//div[@id="newhouse_loupai_list"]/ul/li')

        for house_li in house_content_ul:
            # 楼盘链接  http://guangguzhongxinchengld.fang.com/
            fang_url = house_li.css(
                'div.nlcd_name a::attr(href)').extract_first()
            if fang_url:
                item['item_url'] = fang_url.strip()

            newcode = house_li.css('div.duibi::attr(onclick)').re('(\d+)')

            if newcode:
                item['newcode'] = newcode[0]
            else:
                item['newcode'] = ''

            # 楼盘名称 光谷万科中心
            name = house_li.css('div.nlcd_name a::text').extract_first()
            if name:
                item['ad_name'] = name.strip()

            # 房源地址信息
            relative_message = house_li.css('div.relative_message')
            if relative_message:
                # 楼盘地址 [二至三环]东湖高新区关山大道与南湖大道交汇处（光谷天地旁）
                address = relative_message.css(
                    'div.address a::attr(title)').extract_first()
                if address:
                    item['address'] = address.strip()

                # 区域信息 东湖高新区
                ad_area = relative_message.css(
                    'div.address a span.sngrey::text').extract_first()
                if ad_area and ad_area.find('[') >= 0:
                    item['ad_area'] = ad_area.strip()[1:-1]

            # 房源状态 [在售][住宅][标签]
            fangyuan = house_li.css('div.fangyuan')
            if fangyuan:
                # 销售状态
                item['sales_status'] = fangyuan.css(
                    'span::text').extract_first().strip()

                # 房源类型
                item['property_category'] = fangyuan.css(
                    'a::text').extract_first().strip()

            # 价格
            show_price = house_li.css(
                'div.nhouse_price span::text').extract_first()

            if show_price:
                item['show_price'] = show_price
            else:
                item['show_price'] = '价格待定'

            if item['newcode'] != "":
                # 存储list数据
                yield item

            # if fang_url and item['property_category'].find('住宅') >= 0:
            #     yield scrapy.Request(
            #         url=fang_url, callback=self.parse_xinfang_data)

        # 下一页翻页
        if curPage != totalPage:
            next_page = int(curPage) + 1
            yield scrapy.Request(
                url=response.url.split('b9')[0] + 'b9' + str(next_page) + '/',
                callback=self.parse_xinfang_list)

    def parse_xinfang_data(self, response):
        # 唯一标识
        newcode = response.xpath(
            '//span[@class="mobck"]/a/@href').re("(\d+)")[0]

        # 导航栏
        head = response.css('div.nav')
        if head:
            # 详细信息url
            house_detail_url = head.css(
                'div.navleft a:contains("详")::attr(href)').extract_first()

            # 动态
            house_info_url = head.css(
                'div.navleft a:contains("动态")::attr(href)').extract_first()

            # 户型
            house_type_url = head.css(
                'div.navleft a:contains("户型")::attr(href)').extract_first()

            # 相册
            # house_image_url = head.css(
            #     'div.navleft a:contains("相册")::attr(href)').extract_first()

        # yield detail_item

        if house_detail_url:
            yield scrapy.Request(
                url=house_detail_url, callback=self.parse_house_detail, meta={'newcode': newcode})

        # if house_info_url:
        #     yield scrapy.Request(
        #         url=house_info_url, callback=self.parse_house_info, meta={'newcode': newcode})

        # if house_type_url:
        #     yield scrapy.Request(
        #         url=house_type_url, callback=self.parse_house_type_list, meta={'newcode': newcode})

        # if house_image_url:
        #     yield scrapy.Request(
        #         url=house_image_url, callback=self.parse_house_photo_list, meta={'newcode': newcode})

    # def parse_house_peitao(self, response):
    #     # 配套信息

    def parse_house_detail(self, response):
        '''
            房源详细信息
        '''
        item = house_detail_item()
        #------------------------------ 基本信息 ---------------------------------------- #
        # base_info = response.css('div.main-item h3:contains("基本信息") ~ ul')

        item['item_type'] = 'house_detail'
        item['item_url'] = response.url
        item['newcode'] = response.meta['newcode']

        # 物业类别
        # house_type = response.css(
        #     'div.list-left:contains("物业类别") + div.list-right::text').extract_first()

        # if house_type:
        #     item['house_type'] = house_type.strip()
        # else:
        #     item['house_type'] = ''

        # 楼盘名
        house_adname = response.xpath(
            '//a[@class="ts_linear"]/text()').extract_first()

        if house_adname:
            item['house_adname'] = house_adname
        else:
            item['house_adname'] = ''

        # 建筑类别
        building_type = response.css(
            'div.list-left:contains("建筑类别") + div.list-right span::text').re('\w+')

        if building_type:
            item['building_type'] = "、".join(building_type)
        else:
            item['building_type'] = ''

        # 项目特色
        building_features = response.css(
            'div.list-left:contains("项目特色") + div.list-right span.tag::text').re('\w+')

        if building_features:
            item['building_features'] = "、".join(building_features)
        else:
            item['building_features'] = '暂无特色'

        # 装修状况
        decoration = response.css(
            'div.list-left:contains("装修状况") + div.list-right::text').extract_first()

        if decoration:
            item['decoration'] = decoration.strip()
        else:
            item['decoration'] = ''

        # 产权年限
        property_years = response.css(
            'div.list-left:contains("产权年限") + div.list-right p::text').extract_first()

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
            url = 'http://api.map.baidu.com/geocoder/v2/'
            output = 'json'
            ak = 'EB3b1bbf5514cfae6b1335e72c00dec0'
            add = quote(sales_address.strip())  # 由于本文城市变量为中文，为防止乱码，先用quote进行编码
            uri = url + '?' + 'address=' + add + '&output=' + \
                output + '&ak=' + ak
            req = urllib.request.urlopen(uri)
            res = req.read().decode()  # 将其他编码的字符串解码成unicode
            temp = json.loads(res)  # 对json数据进行解析
        else:
            item['sales_address'] = ''

        # 预售许可证

        #---------------------------------------- 销售信息 ---------------------------------------- #

        #---------------------------------------- 周边设施 ---------------------------------------- #

        # 交通
        traffic = response.xpath("//span[contains(text(),'交通')]/../text()")
        if traffic:
            item['traffic'] = ' '.join(traffic.extract()).strip()

        # 学校
        schoolStr = ''
        kindergarten = response.xpath(
            "//span[contains(text(),'幼儿园')]/../text()")
        if kindergarten:
            schoolStr += '幼儿园:' + ''.join(kindergarten.extract()).strip()

        middle = response.xpath("//span[contains(text(),'中小学')]/../text()")
        if middle:
            schoolStr += '    中小学:' + ''.join(middle.extract()).strip()

        university = response.xpath("//span[contains(text(),'大学')]/../text()")
        if university:
            schoolStr += '    大学:' + ''.join(university.extract()).strip()

        if schoolStr != '':
            item['school'] = schoolStr

        market = response.xpath("//span[contains(text(),'商场')]/../text()")
        if market:
            item['market'] = ''.join(market.extract()).strip()

        hospital = response.xpath("//span[contains(text(),'医院')]/../text()")
        if hospital:
            item['hospital'] = ''.join(hospital.extract()).strip()

        bank = response.xpath("//span[contains(text(),'银行')]/../text()")
        if bank:
            item['bank'] = ''.join(bank.extract()).strip()

        # 价格信息
        trs = response.xpath(
            "//div[@class='main-item']/h3[contains(string(),'价格信息')]/following-sibling::*[1]/div/table/tr")

        if trs:
            item_price = house_price()
            for tr in trs:
                td_value = tr.xpath('td/text()').extract()
                time = td_value[0].strip()
                avg_price = re.findall(r"\d+\.?\d*", td_value[1].strip())
                price_desc = td_value[3].strip()
                if avg_price and avg_price != "" and avg_price != "均价":
                    item_price['item_url'] = response.url
                    item_price['item_type'] = 'house_price'
                    item_price['newcode'] = response.meta['newcode']
                    item_price['time'] = time
                    item_price['avg_price'] = avg_price[0]
                    item_price['price_desc'] = price_desc
                    yield item_price

        #---------------------------------------- 周边设施 ---------------------------------------- #

        # 预售许可证
        ys_trs = response.xpath(
            "//td[contains(string(),'预售许可证')]/../following-sibling::*")

        if ys_trs:
            item_permit = house_permit()
            for tr in ys_trs:
                td_value = tr.xpath('td/text()').extract()
                permit_no = td_value[0].strip()
                permit_time = td_value[1].strip()
                permit_desc = td_value[2].strip()
                if permit_no and permit_no != "" and permit_no != "预售许可证" and permit_no.find('武') >= 0:
                    item_permit['item_url'] = response.url
                    item_permit['item_type'] = 'house_permit'
                    item_permit['newcode'] = response.meta['newcode']
                    item_permit['permit_no'] = permit_no
                    item_permit['permit_time'] = permit_time
                    item_permit['permit_desc'] = permit_desc
                    yield item_permit

        #---------------------------------------- 小区信息 ---------------------------------------- #
        # 占地面积
        land_area = response.css(
            'div.list-left:contains("占地面积") + div.list-right::text').re('(\d+)')

        if land_area:
            item['land_area'] = land_area[0]
        else:
            item['land_area'] = ''

        # 建筑面积
        build_area = response.css(
            'div.list-left:contains("建筑面积") + div.list-right::text').re('(\d+)')

        if build_area:
            item['build_area'] = build_area[0]
        else:
            item['build_area'] = ''

        # 容积率
        volume_rate = response.css(
            'div.list-left:contains("容") + div.list-right::text').re('(\d+(\.\d+)?)')

        if volume_rate:
            item['volume_rate'] = volume_rate[0]
        else:
            item['volume_rate'] = ''

        # 绿化率
        greening_rate = response.css(
            'div.list-left:contains("绿") + div.list-right::text').re('(\d+(\.\d+)?)')

        if volume_rate:
            item['greening_rate'] = greening_rate[0]
        else:
            item['greening_rate'] = ''

        # 停车位
        parking_count = response.css(
            'div.list-left:contains("车") + div.list-right::text').re('(\d+(\.\d+)?)')

        if parking_count:
            item['parking_count'] = parking_count[0]
        else:
            item['parking_count'] = ''

        # 栋总数
        house_count = response.css(
            'div.list-left:contains("户") + div.list-right::text').re('(\d+(\.\d+))')

        if house_count:
            item['house_count'] = house_count[0]
        else:
            item['house_count'] = '暂无资料'

        property_company = response.css(
            'div.list-left:contains("物业公司") + div.list-right a::text').extract_first()

        if property_company:
            item['property_company'] = property_company
        else:
            item['property_company'] = '暂无资料'

        # 物业费
        property_costs = response.css(
            'div.list-left:contains("物") + div.list-right::text').re('(\d+(\.\d+)?)')

        if property_costs:
            item['property_costs'] = property_costs[0]
        else:
            item['property_costs'] = '暂无资料'

        # 物业费描述
        property_costs_description = response.css(
            'div.list-left:contains("物业费描述") + div.list-right-floor::text').extract_first()

        if property_costs_description:
            item['property_costs_description'] = property_costs_description
        else:
            item['property_costs_description'] = '暂无资料'

        #---------------------------------------- 小区信息 ---------------------------------------- #

        #---------------------------------------- 项目简介 ---------------------------------------- #

        project_description = response.css('p.intro::text').extract_first()

        if project_description:
            item['project_description'] = project_description.strip()
        else:
            item['project_description'] = '暂无资料'

        #---------------------------------------- 项目简介 ---------------------------------------- #

        yield item

    def parse_house_info(self, response):
        '''
            房源动态信息 [取第一条]
        '''
        item = house_info_item()
        item['newcode'] = response.meta['newcode']
        item['item_type'] = 'house_info'
        info_date = response.xpath(
            '//div[@id="gushi_blog"]/ul/li[1]/div[1]/text()').extract_first()

        item_url = response.xpath(
            '//div[@id="gushi_blog"]/ul/li[1]/h2/a/@href').extract_first()
        if item_url:
            item['item_url'] = item_url.strip()
        else:
            item['item_url'] = ''

        if info_date:
            item['info_date'] = info_date.strip()
        else:
            item['info_date'] = ''

        info_title = response.xpath(
            '//div[@id="gushi_blog"]/ul/li[1]/h2/a/text()').extract_first()
        if info_title:
            item['info_title'] = info_title.strip()
        else:
            item['info_title'] = ''

        info_detail = response.xpath(
            '//div[@id="gushi_blog"]/ul/li[1]/p/text()').extract_first()
        if info_detail:
            item['info_detail'] = info_detail[:-1].strip()
        else:
            item['info_detail'] = ''

        yield item

    def parse_house_type_list(self, response):
        newcode = response.meta['newcode']
        li_imgids = response.xpath(
            '//li[@class="xc_img_list"]/a/@href').re('_(\d+)')
        baseurl = response.url.split('/')[2]
        for imgid in li_imgids:
            house_type_api = "http://{baseurl}/house/ajaxrequest/getPhotoDetail.php?city=武汉&newcode={newcode}&picid={imgid}".format(
                baseurl=baseurl, newcode=newcode, imgid=imgid)
            yield scrapy.Request(url=house_type_api, callback=self.parse_house_type_detail, meta={"newcode": newcode})

    def parse_house_type_detail(self, response):
        '''
            户型详细信息
        '''
        item = house_type_item()
        results = json.loads(response.text)
        house_type_dict = results.get('thisPic')
        item['item_url'] = response.url
        if house_type_dict:
            # 户型名称
            item['item_type'] = 'house_type'
            item['newcode'] = response.meta['newcode']
            item['house_type_id'] = house_type_dict['id']
            item['house_type_name'] = house_type_dict['hx_title']
            item['house_type_room_cnt'] = house_type_dict['room']
            item['house_type_hall_cnt'] = house_type_dict['hall']
            item['house_type_kitchen_cnt'] = house_type_dict['kitchen']
            item['house_type_toilet_cnt'] = house_type_dict['toilet']
            # 建筑面积
            item['house_type_size'] = house_type_dict['buildingarea']
            # 户型描述
            # item['house_type_desc'] = house_type_dict['hx_desp']
            hx_desp = house_type_dict['hx_desp']
            if hx_desp != "":
                item['house_type_desc'] = hx_desp
            else:
                item['house_type_desc'] = '暂无'

            item['house_type_status'] = house_type_dict['tags'][0]
            item['house_type_image_url'] = house_type_dict['houseimageurl']
        yield item

    # def getlnglat(address):
    #     url = 'http://api.map.baidu.com/geocoder/v2/'
    #     output = 'json'
    #     ak = '你申请的密钥***'
    #     add = address  # 由于本文城市变量为中文，为防止乱码，先用quote进行编码
    #     uri = url + '?' + 'address=' + add + '&output=' + output + '&ak=' + ak
    #     req = urlopen(uri)
    #     res = req.read().decode()  # 将其他编码的字符串解码成unicode
    #     temp = json.loads(res)  # 对json数据进行解析
    #     return temp

    # def parse_house_photo_list(self, response):
    #     '''
    #         图片信息
    #     '''
    #     newcode = response.meta['newcode']
    #     baseurl = response.url.split('/')[2]
    #     types = ['901', '903', '904', '905', '907']
    #     for img_type in types:
    #         house_photo_api = "http://{baseurl}/house/ajaxrequest/hxquanping_get.php?newcode={newcode}&type={types}&nowpicid=1000000&count=100".format(
    #             baseurl=baseurl, newcode=newcode, types=img_type)
    #         yield scrapy.Request(url=house_photo_api, callback=self.parse_house_photo_detail)

    # def parse_house_photo_detail(self, response):
    #     results = json.loads(response.text)
    #     if results.get('resCode'):
    #         pass
    #     else:
    #         list = results.get('list')
    #         for obj in list:
    #             item = house_photo_item()
    #             item['item_url'] = response.url
    #             item['newcode'] = obj['newcode']
    #             item['item_type'] = 'house_photo'
    #             item['house_photo_url'] = obj['url']
    #             item['house_photo_type'] = obj['pictype']
    #             item['house_photo_id'] = obj['id']
    #             item['house_photo_tag'] = obj['tag']
    #         yield item
