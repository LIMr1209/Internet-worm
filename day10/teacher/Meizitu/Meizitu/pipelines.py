# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import ImagesPipeline
import scrapy
import json
class MeizituImagePipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        image = item["image"]
        yield scrapy.Request(image)

    def item_completed(self, results, item, info):
        image_path = [x["path"] for ok, x in results if ok]
        if len(image_path)> 0:
            print("image_path==",image_path)
            item["image_path"] = image_path[0]

        return item





class MeizituPipeline(object):
    def open_spider(self,spider):
        self.file = open(spider.name+".json","w",encoding="utf-8")
    def close_spider(self,spider):
        self.file.close()

    def process_item(self, item, spider):

        self.file.write(json.dumps(dict(item),ensure_ascii=False)+"\n")
        return item
