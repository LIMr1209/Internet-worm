# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class DoubanPipeline(object):
    def open_spider(self,spider):
        #当爬虫开始执行的时候调用
        self.file = open(spider.name+".json","w",encoding="utf-8")
    def process_item(self, item, spider):
        #保存数据
        self.file.write(json.dumps( dict(item),ensure_ascii=False)+"\n")
        return item

    def close_spider(self):
        "当爬虫结束的时候调用，释放资源"
        self.file.close()


