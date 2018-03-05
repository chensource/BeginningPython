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
            # 列表页的数据
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
            # 详情页信息
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
                    self.cursor.execute(insertsql)
                    # 插入数据
                self.conn.commit()
            except Exception as error:
                # 出现错误时打印错误日志
                pass
            return item
        elif item_type == "house_info":
            # 资讯信息
            newcode = item['newcode']
            info_date = item['info_date']
            info_title = item['info_title']
            info_detail = item['info_detail']

            try:
                selectStr = "select * from `{table_name}` where item_url = '{item_url}'".format(
                    table_name=collection_name, item_url=item_url)
                self.cursor.execute(selectStr)
                # 是否有重复数据
                repetition = self.cursor.fetchone()
                if repetition:
                    pass
                else:
                    insertsql = "INSERT INTO `{table_name}` (`newcode`, `item_url`, `item_type`, `info_date`, `info_title`, `info_detail`) VALUES ('{newcode}', '{item_url}', '{item_type}', '{info_date}', '{info_title}', '{info_detail}')".format(
                        table_name=collection_name,
                        newcode=newcode,
                        item_url=item_url,
                        item_type=item_type,
                        info_date=info_date,
                        info_title=info_title,
                        info_detail=info_detail
                    )
                    self.cursor.execute(insertsql)
                self.conn.commit()
            except Exception as error:
                pass
            return item
        elif item_type == "house_type":
            newcode = item['newcode']
            house_type_id = item['house_type_id']
            house_type_name = item['house_type_name']
            room_cnt = item['house_type_room_cnt']
            hall_cnt = item['house_type_hall_cnt']
            kitchen_cnt = item['house_type_kitchen_cnt']
            toilet_cnt = item['house_type_toilet_cnt']
            size = item['house_type_size']
            desc = item['house_type_desc']
            status = item['house_type_status']
            image_url = item['house_type_image_url']
            # 户型信息
            try:
                selectStr = "select * from `{table_name}` where house_type_id = '{house_type_id}'".format(
                    table_name=collection_name,
                    house_type_id=house_type_id
                )
                self.cursor.execute(selectStr)
                # 是否有重复数据
                repetition = self.cursor.fetchone()
                if repetition:
                    updatesql = "UPDATE `{table_name}` SET `name`='{name}', `room_cnt`='{room_cnt}', `hall_cnt`='{hall_cnt}', `kitchen_cnt`='{kitchen_cnt}', `toilet_cnt`='{toilet_cnt}', `size`='{size}', `desc`='{desc}', `status`='{status}', `image_url`='{image_url}' WHERE (`house_type_id`='{house_type_id}')".format(
                        table_name=collection_name,
                        house_type_id=house_type_id,
                        name=house_type_name,
                        room_cnt=room_cnt,
                        hall_cnt=hall_cnt,
                        kitchen_cnt=kitchen_cnt,
                        toilet_cnt=toilet_cnt,
                        size=size,
                        desc=desc,
                        status=status,
                        image_url=image_url
                    )
                    self.cursor.execute(updatesql)
                else:
                    insertsql = "INSERT INTO `{table_name}` (`house_type_id`, `newcode`, `item_type`, `item_url`, `name`, `room_cnt`, `hall_cnt`, `kitchen_cnt`, `toilet_cnt`, `size`, `desc`, `status`, `image_url`) VALUES('{house_type_id}', '{newcode}', '{item_type}', '{item_url}', '{name}', '{room_cnt}', '{hall_cnt}', '{kitchen_cnt}', '{toilet_cnt}', '{size}', '{desc}', '{status}', '{image_url}')".format(
                        table_name=collection_name,
                        house_type_id=house_type_id,
                        newcode=newcode,
                        item_type=item_type,
                        item_url=item_url,
                        name=house_type_name,
                        room_cnt=room_cnt,
                        hall_cnt=hall_cnt,
                        kitchen_cnt=kitchen_cnt,
                        toilet_cnt=toilet_cnt,
                        size=size,
                        desc=desc,
                        status=status,
                        image_url=image_url
                    )
                    self.cursor.execute(insertsql)
                self.conn.commit()
            except Exception as error:
                pass
            return item
        # elif item_type == "house_type":
        #     try:
        #         photo_id = item['house_photo_id']
        #         newcode = item['newcode']
        #         photo_url = item['house_photo_url']
        #         photo_type = item['house_photo_type']
        #         photo_tag = item['house_photo_tag']
        #         selectStr = "select * from `{table_name}` where photo_id = '{photo_id}'".format(
        #             table_name=collection_name,
        #             photo_id=photo_id
        #         )
        #         self.cursor.execute(selectStr)
        #         # 是否有重复数据
        #         repetition = self.cursor.fetchone()
        #         if repetition:
        #             pass
        #             # 更新数据
        #         else:
        #             # 添加数据
        #             insertsql = "INSERT INTO `{table_name}` (`photo_id`, `newcode`, `item_type`, `item_url`, `photo_tag`, `photo_url`, `photo_type`) VALUES ('{photo_id}', '{newcode}', '{item_type}', '{item_url}','{photo_tag}', '{photo_url}', '{photo_type}')".format(
        #                 table_name=collection_name,
        #                 photo_id=photo_id,
        #                 newcode=newcode,
        #                 item_type=item_type,
        #                 item_url=item_url,
        #                 photo_url=photo_url,
        #                 photo_type=photo_type,
        #                 photo_tag=photo_tag
        #             )
        #             self.cursor.execute(insertsql)
        #         self.conn.commit()
        #     except Exception as error:
        #         pass
        elif item_type == "house_price":
            try:
                newcode = item['newcode']
                price_time = item['time']
                avg_price = item['avg_price']
                price_desc = item['price_desc']

                selectStr = "select * from `{table_name}` where `price_time` = '{price_time}' AND `price_avg` = '{avg_price}' AND `newcode` = '{newcode}' ".format(
                    table_name=collection_name,
                    price_time=price_time,
                    avg_price=avg_price,
                    newcode=newcode
                )
                self.cursor.execute(selectStr)
                # 是否有重复数据
                repetition = self.cursor.fetchone()

                if repetition:
                    pass
                else:
                    insertsql = "INSERT INTO `{table_name}` (`item_type`, `newcode`, `price_time`, `price_avg`, `price_desc`) VALUES ('{item_type}','{newcode}', '{price_time}', '{price_avg}', '{price_desc}')".format(
                        table_name=collection_name,
                        item_type=item_type,
                        newcode=newcode,
                        price_time=price_time,
                        price_avg=avg_price,
                        price_desc=price_desc
                    )
                    self.cursor.execute(insertsql)
                self.conn.commit()
            except Exception as error:
                pass
        else:
            try:
                newcode = item['newcode']
                permit_no = item['permit_no']
                permit_time = item['permit_time']
                permit_desc = item['permit_desc']

                selectStr = "select * from `{table_name}` where `permit_no` = '{permit_no}' AND `permit_time` = '{permit_time}' AND `newcode` = '{newcode}' ".format(
                    table_name=collection_name,
                    permit_no=permit_no,
                    permit_time=permit_time,
                    newcode=newcode
                )
                self.cursor.execute(selectStr)
                # 是否有重复数据
                repetition = self.cursor.fetchone()

                if repetition:
                    pass
                else:
                    insertsql = "INSERT INTO `{table_name}` (`item_type`, `newcode`, `permit_no`, `permit_time`, `permit_desc`) VALUES ('{item_type}', '{newcode}', '{permit_no}', '{permit_time}', '{permit_desc}')".format(
                        table_name=collection_name,
                        item_type=item_type,
                        newcode=newcode,
                        permit_no=permit_no,
                        permit_time=permit_time,
                        permit_desc=permit_desc
                    )
                    self.cursor.execute(insertsql)
                self.conn.commit()
            except Exception as error:
                pass

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
