# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import mysql.connector
from scrapy import log
from fang_link.items import fang_list_item, house_detail_item, house_info_item, house_type_item, house_photo_item
import time


class MysqlPipeline:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host='10.25.200.207',
            port='3306',
            user='root',
            password='P@ssw0rdWh',
            database='fang_db')
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        collection_name = item['item_type']
        item_url = item['item_url']
        item_type = item['item_type']
        UpdateTime = time.strftime(
            '%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        if item_type == "house_list":
            try:
                # 查重处理
                newcode = item['newcode']
                selectStr = "select * from `{table_name}` where newcode = '{newcode}'".format(
                    table_name=collection_name, newcode=newcode)
                self.cursor.execute(selectStr)
                # 是否有重复数据
                repetition = self.cursor.fetchone()
                ad_name = item['ad_name']
                address = item['address']
                ad_area = item['ad_area']
                sales_status = item['sales_status']
                property_category = item['property_category']
                show_price = item['show_price']
                # 重复
                if repetition:
                    updatesql = "UPDATE `{table_name}` SET `item_url`='{item_url}',`item_type`= '{item_type}',`ad_name`= '{ad_name}',`address`= '{address}',`ad_area`= '{ad_area}',`sales_status`= '{sales_status}',`property_category`= '{property_category}',`show_price`= '{show_price}' WHERE (`newcode`='{newcode}') ".format(
                        table_name=collection_name,
                        item_url=item_url,
                        item_type=item_type,
                        ad_name=ad_name,
                        address=address,
                        ad_area=ad_area,
                        sales_status=sales_status,
                        property_category=property_category,
                        show_price=show_price,
                        newcode=newcode
                    )
                    self.cursor.execute(updatesql)
                else:
                    # 插入数据
                    insertsql = "INSERT INTO `{table_name}`(`newcode`, `item_url`, `item_type`, `ad_name`, `address`, `ad_area`, `sales_status`, `property_category`, `show_price`)VALUES('{newcode}', '{item_url}', '{item_type}', '{ad_name}', '{address}','{ad_area}', '{sales_status}', '{property_category}', '{show_price}')".format(
                        table_name=collection_name,
                        newcode=newcode,
                        item_url=item_url,
                        item_type=item_type,
                        ad_name=ad_name,
                        address=address,
                        ad_area=ad_area,
                        sales_status=sales_status,
                        property_category=property_category,
                        show_price=show_price)
                    self.cursor.execute(insertsql)
                # 提交sql语句
                self.conn.commit()
            except Exception as error:
                # 出现错误时打印错误日志
                pass
            return item
        elif item_type == "house_detail":
            try:
                newcode = item['newcode']
                building_type = item['building_type']
                building_features = item['building_features']
                decoration = item['decoration']
                property_years = item['property_years']
                loop_location = item['loop_location']
                developer = item['developer']
                sales_status = item['sales_status']
                opening_time = item['opening_time']
                delivery_time = item['delivery_time']
                sales_address = item['sales_address']
                land_area = item['land_area']
                build_area = item['build_area']
                volume_rate = item['volume_rate']
                greening_rate = item['greening_rate']
                parking_count = item['parking_count']
                house_count = item['house_count']
                property_company = item['property_company']
                property_costs = item['property_costs']
                property_costs_description = item['property_costs_description']
                project_description = item['project_description']

                selectStr = "select * from `{table_name}` where newcode = '{newcode}'".format(
                    table_name=collection_name, newcode=newcode)
                self.cursor.execute(selectStr)
                # 是否有重复数据
                repetition = self.cursor.fetchone()
                if repetition:
                    # 更新数据
                    updatesql = "UPDATE `{table_name}` SET `item_url`='{item_url}', `building_type`='{building_type}', `building_features`='{building_features}', `decoration`='{decoration}', `property_years`='{property_years}', `loop_location`='{loop_location}', `developer`='{developer}', `opening_time`='{opening_time}', `delivery_time`='{delivery_time}', `sales_address`='{sales_address}', `land_area`='{land_area}', `build_area`='{build_area}', `volume_rate`='{volume_rate}', `greening_rate`='{greening_rate}', `parking_count`='{parking_count}',`house_count`='{house_count}', `property_company`='{property_company}', `property_costs`='{property_costs}', `project_description`='{project_description}',`UpdateTime`='{UpdateTime}' WHERE (`newcode`='{newcode}')".format(
                        table_name=collection_name,
                        newcode=newcode,
                        item_url=item_url,
                        building_type=building_type,
                        building_features=building_features,
                        decoration=decoration,
                        property_years=property_years,
                        loop_location=loop_location,
                        developer=developer,
                        opening_time=opening_time,
                        delivery_time=delivery_time,
                        sales_address=sales_address,
                        land_area=land_area,
                        build_area=build_area,
                        volume_rate=volume_rate,
                        greening_rate=greening_rate,
                        parking_count=parking_count,
                        house_count=house_count,
                        property_company=property_company,
                        property_costs=property_costs,
                        project_description=project_description,
                        UpdateTime=UpdateTime
                    )
                    print(updatesql)
                    self.cursor.execute(updatesql)
                else:
                    insertsql = "INSERT INTO `{table_name}` (`newcode`, `item_type`, `item_url`, `building_type`, `building_features`, `decoration`, `property_years`, `loop_location`, `developer`, `opening_time`, `delivery_time`, `sales_address`, `land_area`, `build_area`, `volume_rate`, `greening_rate`, `parking_count`, `house_count`, `property_company`, `property_costs`, `property_costs_description`, `project_description`) VALUES ('{newcode}', '{item_type}', '{item_url}', '{building_type}', '{building_features}', '{decoration}', '{property_years}', '{loop_location}', '{developer}', '{opening_time}', '{delivery_time}', '{sales_address}', '{land_area}', '{build_area}', '{volume_rate}', '{greening_rate}', '{parking_count}', '{house_count}', '{property_company}', '{property_costs}', '{property_costs_description}', '{project_description}')".format(
                        table_name=collection_name,
                        newcode=newcode,
                        item_type=item_type,
                        item_url=item_url,
                        building_type=building_type,
                        building_features=building_features,
                        decoration=decoration,
                        property_years=property_years,
                        loop_location=loop_location,
                        developer=developer,
                        opening_time=opening_time,
                        delivery_time=delivery_time,
                        sales_address=sales_address,
                        land_area=land_area,
                        build_area=build_area,
                        volume_rate=volume_rate,
                        greening_rate=greening_rate,
                        parking_count=parking_count,
                        house_count=house_count,
                        property_company=property_company,
                        property_costs=property_costs,
                        property_costs_description=property_costs_description,
                        project_description=project_description
                    )
                    print(insertsql)
                    self.cursor.execute(insertsql)
                    # 插入数据
                self.conn.commit()
            except Exception as error:
                # 出现错误时打印错误日志
                pass
            return item
        elif item_type == "":
            pass
        else:
            pass
        newcode = item['newcode']

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()


# class MongoPipeline(object):
#     def __init__(self, mongo_uri, mongo_db):
#         self.mongo_uri = mongo_uri
#         self.mongo_db = mongo_db

#     @classmethod
#     def from_crawler(cls, crawler):
#         return cls(
#             mongo_uri=crawler.settings.get('MONGO_URI'),
#             mongo_db=crawler.settings.get('MONGO_DB')
#         )

#     def open_spider(self, spider):
#         self.client = pymongo.MongoClient(self.mongo_uri)
#         self.db = self.client[self.mongo_db]

#     def close_spider(self, spider):
#         self.client.close()

#     def process_item(self, item, spider):
#         # 加入对应的表
#         collection_name = item['item_type']
#         # 直接进行更新操作，附带去重功能
#         if item['newcode'] != '':
#             self.db[collection_name].update(
#                 {'newcode': item['newcode']}, {'$set': item}, True)
#             return item
