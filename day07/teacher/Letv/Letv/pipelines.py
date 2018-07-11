# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import ImagesPipeline
import scrapy


class LetvImagePipeline(ImagesPipeline):
    # def process_item(self, item, spider):
    #     return item
    def get_media_requests(self, item, info):
        # 得到图片链接
        image_path = item["image"]
        print("image_path===", image_path)
        # 把图片的链接交引擎
        yield scrapy.Request(image_path)


class LetvPipeline(object):
    def process_item(self, item, spider):
        return item
