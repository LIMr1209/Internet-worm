# -*- coding: utf-8 -*-
import json


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MyspiderPipeline(object):
    def process_item(self, item, spider):
        return item


# settings  中  ITEM_PIPELINES 列表中配置    'mySpider.pipelines.AtguiguPipeline': 300,
class AtguiguPipeline(object):
    def __init__(self):
        self.file = open('atguigu.json', 'w', encoding='utf-8')

    def open_spider(self, spider):  # 方法名不能写错 要有spider参数
        print('开始爬取')

    def process_item(self, item, spider):  # 方法名不能写错 要有spider参数，item
        item_dict = dict(item)
        json_object = json.dumps(item_dict, ensure_ascii=False) + '\n'
        self.file.write(json_object)
        return item  # 需要返回

    def close_spider(self, spider):  # 方法名不能写错 要有spider参数
        print('结束爬取')
        self.file.close()
