# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
from pymongo import MongoClient
from Tencent.settings import MONGO_HOST
from Tencent.settings import MONGO_PORT
from Tencent.settings import MONGO_DBNAME
from Tencent.settings import SHEET_NAME


class TencentPositionPipeline(object):
    """把数据保存到mongodb数据库"""
    def open_spider(self, spider):
        #得到的实例对象是MongoClient
        client = MongoClient(MONGO_HOST,MONGO_PORT)
        #创建数据库成功，Tencent
        dbname = client[MONGO_DBNAME]

        #集合tencentPosition
        self.collection = dbname[SHEET_NAME]


    def process_item(self, item, spider):

        #转换成python的字典
        pyhton_dict = dict(item)

        #插入数据,字典
        self.collection.insert_one(pyhton_dict)

        return item

    def close_spider(self, spider):
        pass


class TencentPipeline(object):
    #传入的spider是TencentpositionSpider的实例对象
    def open_spider(self,spider):
        print(spider.name, "开始运行了......................")
        #当爬虫开始运行的时候，创建TencentPosition.json
        self.file_name = open(spider.name+".json","w")

    def process_item(self, item, spider):
        print("item===",item)
        #python的字典（object）
        python_dict = dict(item)

        #字符串
        json_text = json.dumps(python_dict,ensure_ascii=False)+"\n"


        self.file_name.write(json_text)
        # item["postion_link"] = "你真坏"
        return item

    def close_spider(self,spider):
        print(spider.name,"运行结束了..................")

class AtguiguPipeline(object):
    #传入的spider是TencentpositionSpider的实例对象
    def open_spider(self,spider):
        print(spider.name, "开始运行了......................")
        #当爬虫开始运行的时候，创建TencentPosition.json
        self.file_name = open(spider.name+"_atguiugu.xml","w")

    def process_item(self, item, spider):
        print("item===",item)
        #python的字典（object）
        python_dict = dict(item)

        #字符串
        json_text = json.dumps(python_dict,ensure_ascii=False)+"\n"


        self.file_name.write(json_text)
        return item

    def close_spider(self,spider):
        print(spider.name,"运行结束了..................")


