# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import requests

class Meizitu2Pipeline(object):
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
    def process_item(self, item, spider):

        if "image_urls" in item:

            #把下载的图片的路径得到
            image_paths = []
            for image in item["image_urls"]:

                print("image===",image)
                #http://mm.chinasareview.com/wp-content/uploads/2017a/07/18/01.jpg
                if not os.path.exists("./Image/"):
                    os.makedirs("./Image/")

                #图片保存路径
                image_path = "./Image/"+image[7:].replace("/","_")


                if  not os.path.exists(image_path):

                    #下载图片
                    response = requests.get(image,headers=self.headers)

                    if response.status_code == 200:
                        with open(image_path,"wb") as f:
                            #保存图片
                            f.write(response.content)

                # 添加图片保存路径
                image_paths.append(image_path)

            item["image_paths"] = image_paths



        return item
