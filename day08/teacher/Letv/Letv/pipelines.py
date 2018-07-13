# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.pipelines.images import ImagesPipeline
#保存图片
import json
import os
from Letv.settings import IMAGES_STORE
# from scrapy.utils.project import get_project_settings
class LetvImagePipeline(ImagesPipeline):
    # IMAGES_STORE = get_project_settings().get("IMAGES_STORE")

    #添加请求图片的路径
    def get_media_requests(self, item, info):
        #图片下载路径
        image = item["image"]
        #把图片路径添加到scrapy引擎里面，让对应的下载器帮我们下载图片
        yield scrapy.Request(image)

    #当图片下载完成后，会调用的方法，并且把下载后的路径，回传到这个方法里
    def item_completed(self, results, item, info):
        print("results===",results)

        # for isTrue,data in results:
        #     print("isTrue===",isTrue)
        #     print("data====",data)
        #     if isTrue:
        #         image = data["path"]
        #         print("image====",image)

        #列表推导式
        image =  [x["path"] for ok,x in results if ok ][0]
        print(image)




        #保存后的路径
        # image = [x["path"] for ok, x in results if ok][0]#full/0a70114884169cbb929ff3960a0ccf3def4c13d0.jpg

        #把图片的名字重命名
        #./images/full/0a70114884169cbb929ff3960a0ccf3def4c13d0.jpg

        old_image_name = IMAGES_STORE+"/"+image
        #./images/黑作坊丶小美儿.jpg
        new_image_name = IMAGES_STORE+"/"+item["nick"]+".jpg"

        print("old_image_name==",old_image_name)
        print("new_image_name==",new_image_name)
        #重命名
        os.rename(old_image_name,new_image_name)

        print(image)
        item["image_path"] = new_image_name

        return item


#默认是处理文本
class LetvPipeline(object):
    #爬虫开始执行的时候调用
    def open_spider(self,spider):
        self.file = open(spider.name+".json","w")

    def process_item(self, item, spider):

        python_dict = dict(item)

        #pyhton 字典-->pyhton str
        json_str = json.dumps(python_dict,ensure_ascii=False)+"\n"
        self.file.write(json_str)
        return item

    #当爬虫结束的时候调用
    def close_spider(self,spider):
        self.file.close()
