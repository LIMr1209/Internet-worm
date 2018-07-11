# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class AtguiguPipeline(object):
    #爬虫开始运行的时候，这个类被实例化
    # def __init__(self):
    #     pass


    #当爬虫开始执行的时候调用
    def open_spider(self,spider):
        print("open_spider---当爬虫开始执行的时候调用")
        print(spider)
        self.file = open("teachers.json", "w")

    #每当yield返回数据的时候，该方法被调用
    #item 就是MyspiderItem类的实例
    def process_item(self, item, spider):
        print("AtguiguPipeline=====",item)
        # python对象
        dict_item = dict(item)
        # python对象转换成str
        json_text = json.dumps(dict_item,ensure_ascii=False)+"\n"

        #保存字符串
        self.file.write(json_text)
        return item

    #爬虫接结束的时候调用该方法
    def close_spider(self,spider):
        print("close_spider --爬虫接结束的时候调用该方法")
        print(spider)
        self.file.close()
