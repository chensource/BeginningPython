# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class fang_list_item(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 实体类型
    item_type = 'list'
    # 唯一标识 [url]
    fang_url = Field()
    # 楼盘名称
    ad_name = Field()
    # 楼盘地址
    address = Field()
    # 楼盘区域
    ad_area = Field()
    # 楼盘板块
    ad_region = Field()
    # 环线位置
    loop_location = Field()
    # 销售状态
    sales_status = Field()
    # 物业类别 [住宅、别墅]
    property_category = Field()
    # 项目特色 [经济住宅、景观居所]
    features = Field()
    # 显示楼盘价格
    show_price = Field()


class fang_detail_item(Item):
    item_type = 'detail'
    # 唯一标识
    fang_url = Field()
    # 房源详情页地址
    house_detail_url = Field()
    # 房源相册地址
    house_image_url = Field()
    # 房源动态地址
    house_info_url = Field()
    # 房源户型地址
    house_type_url = Field()
    # 房价
    house_price_url = Field()
    # # 主力户型
    # main_house_type_str = Field()

    # house_type_detail
    # 户型名称
    house_type_name = Field()
    # 户型地址
    house_type_url = Field()
    # 室
    house_type_room_cnt = Field()
    # 厅
    house_type_hall_cnt = Field()
    # 厨
    house_type_kitchen_cnt = Field()
    # 卫
    house_type_toilet_cnt = Field()
    # 面积
    house_type_size = Field()
    # 描述
    house_type_desc = Field()

    # 图片链接
    img_list = Field()
    # 房源标签
    house_tag = Field()


class house_detail_item(Item):
    # 建筑类别
    build_category = Field()
    # 装修情况
    decoration = Field()
    # 产权年限
    property_years = Field()
    #  开发商
    developer = Field()
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
    house_count = Field()
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
