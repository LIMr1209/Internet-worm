# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class MysinaPipeline(object):
    def open_spider(self, spider):
        self.file = open(spider.name + '.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        print('son_url-------',item['son_url'])
        sub_file_name = item['sub_file_name']
        content = item['content']
        if len(content) > 0:
            print(content)
            file_name = item['son_url']
            file_name = file_name[7:file_name.rfind(".")].replace("/", "_")
            file_path = sub_file_name + "/" + file_name + ".txt"
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
                item['son_path'] = file_path
        self.file.write(json.dumps(dict(item), ensure_ascii=False) + '\n')

        return item

    def close_spider(self, spider):
        self.file.close()
