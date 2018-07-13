# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class DongguanPipeline(object):
    def open_spider(self,spider):
        #创建文件
        self.file = open(spider.name+".json","w",encoding="utf-8")

    def process_item(self, item, spider):

        #python字典
        python_dict = dict(item)
        #python的str
        python_str = json.dumps(python_dict,ensure_ascii=False)+"\n"

        self.file.write(python_str)

        return item

    def close_spider(self,spider):
        self.file.close()
