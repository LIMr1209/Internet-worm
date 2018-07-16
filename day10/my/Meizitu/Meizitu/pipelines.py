# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import requests
import json
from scrapy.pipelines.images import ImagesPipeline
import scrapy


class MeizituPipeline(object):
    headers = {
        'Host': 'mm.chinasareview.com',
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Referer': 'http://www.meizitu.com/a/5585.html',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie': '__jsluid=14600d3c4078768577d30aceeb875172',
        'If-None-Match': '"46a89da2724ed31:10e4"',
        'If-Modified-Since': 'Thu, 26 Oct 2017 15:53:58 GMT',
    }

    def open_spider(self, spider):
        self.file = open(spider.name + '.json', 'w', encoding='utf-8')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        if 'image_urls' in item:
            image_paths = []
            for image in item['image_urls']:
                if not os.path.exists('./Images'):
                    os.mkdir('./Images')
                image_path = "./Images/" + image[7:].replace("/", "_")
                if not os.path.exists(image_path):
                    response = requests.get(image, headers=self.headers)
                    if response.status_code == 200:
                        with open(image_path, 'wb') as f:
                            f.write(response.content)
                image_paths.append(image_path)
            item['image_paths'] = image_paths
            dict_item = dict(item)
            json_obj = json.dumps(dict_item, ensure_ascii=False) + '\n'
            self.file.write(json_obj)
        return item


class Meizitu2Pipeline(object):
    def open_spider(self, spider):
        self.file = open(spider.name + ".json", "w", encoding="utf-8")

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        self.file.write(json.dumps(dict(item), ensure_ascii=False) + "\n")
        return item

class MeizituImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        image_urls = item["image_urls"]
        for urls in image_urls:
            yield scrapy.Request(urls)

    def item_completed(self, results, item, info):
        image_path = [x["path"] for ok, x in results if ok]
        if len(image_path)>0:
            item["image_path"] = image_path[0]
        return item