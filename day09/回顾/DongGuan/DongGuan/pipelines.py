# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from DongGuan.settings import MONGO_PORT, MONGO_HOST, MONGO_DBNAEM, MONGO_SHEETNAME
from pymongo import MongoClient


class MongoPipeline(object):
    def open_spider(self, spider):
        client = MongoClient(MONGO_HOST, MONGO_PORT)
        dbname = client[MONGO_DBNAEM]
        self.collection = dbname[MONGO_SHEETNAME]

    def process_item(self, item, spider):
        dict_item = dict(item)
        self.collection.insert_one(dict_item)
        return item

    def close_spider(self, spider):
        print('....')


class DongguanPipeline(object):
    def open_spider(self, spider):
        self.file = open(spider.name + '.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        dict_item = dict(item)
        json_obj = json.dumps(dict_item, ensure_ascii=False) + "\n"
        self.file.write(json_obj)
        return item

    def close_spider(self, spider):
        self.file.close()
