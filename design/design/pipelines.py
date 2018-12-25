# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#
# from pymongo import MongoClient
# from design.settings import MONGODB_HOST, MONGODB_PORT, MONGODB_DBNAME, SHEETE_NAME
import requests


class ImagePipeline(object):
    def __init__(self):
        # self.url = 'http://opalus.taihuoniao.com/api/image/submit'
        self.url = 'http://127.0.0.1:8002/api/image/submit'

    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):
        dict_item = dict(item)
        response = requests.post(self.url,data=dict_item)
        print(response.content)

    def close_spider(self, spider):
        pass
