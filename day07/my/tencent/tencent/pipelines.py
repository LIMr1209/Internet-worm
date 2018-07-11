# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class TencentPipeline(object):

    def open_spider(self, spider):
        print('开始爬取')
        self.file = open(spider.name + '.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        dict_item = dict(item)
        json_obj = json.dumps(dict_item, ensure_ascii=False) + '\n'
        self.file.write(json_obj)
        # item['position_name'] = '垃圾，快'
        return item

    def close_spider(self, spider):
        print('结束爬取')
        self.file.close()
