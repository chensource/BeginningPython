# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class fang_list_item(Item):
    # 实体类型
    item_type = Field()
    # 房源编号
    newcode = Field()
    # 唯一标识 [url]
    item_url = Field()
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


class house_detail_item(Item):
    # 房源编号
    newcode = Field()
    # 实体类型
    item_type = Field()
    # 页面连接
    item_url = Field()
    # 楼盘名
    house_adname = Field()
    # 建筑类别
    building_type = Field()
    # 项目特色
    building_features = Field()
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
    # presale_permit = Field()
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

    # 周边设施_学校
    school = Field()
    # 周边设施_商场
    market = Field()
    # 周边设施_医院
    hospital = Field()
    # 周边设施_银行
    bank = Field()
    # 其他
    other = Field()
    # 周边设施_交通
    traffic = Field()


class house_info_item(Item):
    '''
    房源资讯信息
    '''
    # 房源状态实体类型
    item_type = Field()
    # 资讯连接
    item_url = Field()
    # 房源信息
    newcode = Field()
    # 资讯时间
    info_date = Field()
    # 资讯标题
    info_title = Field()
    # 资讯详情
    info_detail = Field()


class house_type_item(Item):
    '''
    房源户型信息
    '''
    # 户型id
    house_type_id = Field()
    newcode = Field()
    # 户型连接
    item_url = Field()
    # 状态
    item_type = Field()
    # 户型名称
    house_type_name = Field()
    # 户型地址
    # house_type_url = Field()
    # 室
    house_type_room_cnt = Field()
    # 厅
    house_type_hall_cnt = Field()
    # 厨
    house_type_kitchen_cnt = Field()
    # 卫
    house_type_toilet_cnt = Field()
    # 建筑面积
    house_type_size = Field()
    # 实用面积
    house_type_living_size = Field()
    # 户型描述
    house_type_desc = Field()
    # 主力户型
    house_type_ismain = Field()
    # 总价
    house_type_totalprice = Field()
    # 户型状态
    house_type_status = Field()
    # houseimageurl
    house_type_image_url = Field()


class house_photo_item(Item):
    '''
    房源图片信息
    '''
    item_type = Field()
    item_url = Field()
    # 房源编码
    newcode = Field()
    house_photo_id = Field()
    # 图片连接
    house_photo_url = Field()
    # 图片类型
    house_photo_type = Field()
    # 图片标题
    house_photo_title = Field()
    # 房源标签
    house_photo_tag = Field()


# 价格
class house_price(Item):
    item_type = Field()
    item_url = Field()
    newcode = Field()

    # time
    time = Field()
    avg_price = Field()
    price_desc = Field()


# 预售许可证
class house_permit(Item):
    item_type = Field()
    item_url = Field()
    newcode = Field()

    permit_no = Field()
    permit_time = Field()
    permit_desc = Field()
