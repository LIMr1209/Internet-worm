# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

#后期用到，把数据存储，jons,mysql,mongodb,redis
class MyspiderPipeline(object):
    def process_item(self, item, spider):
        return item
