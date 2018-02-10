# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class FangInfoItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 楼盘名称
    adname = Field()
    # 楼盘价格
    unit_price = Field()
    # 楼盘地址
    address = Field()
    # 物业类别
    property_category = Field()
    # 项目特色
    features = Field()
    # 建筑类别
    build_category = Field()
    # 装修情况
    decoration = Field()
    # 产权年限
    property_years = Field()
    # 环线位置
    loop_location = Field()
    #  开发商
    developer = Field()
    # 销售状态
    sales_status = Field()
    # 开盘时间
    opening_time = Field()
    # 交房时间
    delivery_time = Field()
    # 售楼地址
    sales_address = Field()
    # 预售许可证
    presale_permit = Field()
    # 周边设施_交通
    traffic = Field()
    # 周边设施_学校
    school = Field()
    # 周边设施_商场
    mall = Field()
    # 周边设施_医院
    hospital = Field()
    # 周边设施_银行
    bank = Field()
    # 占地面积
    land_area = Field()
    # 建筑面积
    build_area = Field()
    # 容积率
    volume_rate = Field()
    # 绿化率
    greening_rate = Field()
    # 停车位
    parking_count = Field()
    # 栋座总数
    build_count = Field()
    # 总户数
    House_count = Field()
    # 物业公司
    property_company = Field()
    # 物业费
    property_costs = Field()
    # 物业费描述
    property_costs_description = Field()
    # 楼层情况
    floor_description = Field()
    # 价格信息
    price_time = Field()
    # 价格均价
    price_unit = Field()
    # 起始价格
    price_start = Field()
    # 价格描述
    price_description = Field()
    # 项目简介
    project_description = Field()
    # 图片链接
    img_list = Field()
    # 房源标签
    house_tag = Field()
    # 搜房唯一id
    fang_id = Field()
