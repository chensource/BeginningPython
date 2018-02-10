# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os


class ShupingPipeline(object):
    def process_item(self, item, spider):
        base_dir = os.getcwd()
        file_name = base_dir + '/SP.txt'
        with open(file_name, 'a', encoding='utf-8') as f:
            if item['sec_num'] == '0':
                f.write('时间：' + item['time'] + '\n'
                        '赞同数：' + item['agree'] + '\n'
                        '二级评论数量：' + item['sec_num'] + '\n'
                        '一级评论内容：' + item['fir_text'] + '\n\n'
                        )
            else:
                f.write('时间：' + item['time'] + '\n'
                        '赞同数：' + item['agree'] + '\n'
                        '二级评论数量：' + item['sec_num'] + '\n'
                        '一级评论内容：' + item['fir_text'] + '\n'
                        '二级评论内容：' + '\n'.join(item['sec_text']) + '\n\n'
                        )
        return item
