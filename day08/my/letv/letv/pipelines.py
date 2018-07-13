# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


from scrapy.pipelines.images import ImagesPipeline
import scrapy
import json
from letv.settings import IMAGES_STORE
import os


# from scrapy.utils.project import get_project_settings
class LetvImagePipeline(ImagesPipeline):
    # IMAGES_STORE = get_project_settings().get("IMAGES_STORE")
    def get_media_requests(self, item, info):
        image_url = item['image']
        yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        # results [(True,{'path':'....','url':'......',..})]
        image_path = [x['path'] for ok, x in results if ok][0]  # 得到图片下载路径
        print(image_path)
        old_image_name = IMAGES_STORE + "/" + image_path
        new_image_name = IMAGES_STORE + "/" + item["nick"] + ".jpg"
        os.rename(old_image_name, new_image_name)  # 重命名目录
        item["image_path"] = new_image_name
        # 给item增加这个字段,如果没有写,外界将没有这个字段
        return item


class LetvPipeline(object):
    def open_spider(self, spider):
        print('开始爬取')
        self.file = open(spider.name + '.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        item_dict = dict(item)
        json_obj = json.dumps(item_dict, ensure_ascii=False)
        self.file.write(json_obj)
        return item

    def close_spider(self, spider):
        self.file.close()
        print('结束爬取')
