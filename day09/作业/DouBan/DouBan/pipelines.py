# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.conf import settings
import json
from pymongo import MongoClient


class MongoPipeline(object):
    def open_spider(self, spider):
        client = MongoClient(settings['MONGO_HOST'], settings['MONGO_PORT'])
        dbname = client[settings['MONGO_DBNAME']]
        self.collection = dbname[settings['MONGO_SHEETNAME']]

    def process_item(self, item, spider):
        dict_item = dict(item)
        self.collection.insert_one(dict_item)
        return item

    def close_spider(self, spider):
        print("保存数据库完成")


class DoubanPipeline(object):
    def open_spider(self, spider):
        self.file = open(spider.name + '.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        dict_item = dict(item)
        json_obj = json.dumps(dict_item, ensure_ascii=False) + '\n'
        self.file.write(json_obj)
        return item

    def close_spider(self, spider):
        self.file.close()
