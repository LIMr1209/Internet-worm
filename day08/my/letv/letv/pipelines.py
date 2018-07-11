# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


from scrapy.pipelines.images import ImagesPipeline
import scrapy
import json

class LetvImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        image_path = item['image']
        yield scrapy.Request(image_path)


class LetvPipeline(object):
    def open_spider(self, spider):
        print('开始爬取')
        self.file = open(spider.name + '.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        item_dict = dict(item)
        json_obj = json.dumps(item_dict,ensure_ascii=False)
        self.file.write(json_obj)
        return item

    def close_spider(self, spider):
        self.file.close()
        print('结束爬取')
