# -*- coding: utf-8 -*-
import scrapy

import json

from Letv.items import LetvItem


class LetvliveSpider(scrapy.Spider):
    name = 'LetvLive'
    allowed_domains = ['letv.com']

    pre = "http://dynamic.live.app.m.letv.com/android/dynamic.php?luamod=main&mod=live&ctl=liveHuya&act=channelList&pcode=010210000&version=7.17&channelId=2168&pages="
    suf = "&country=CN&provinceid=1&districtid=9&citylevel=1&location=%E5%8C%97%E4%BA%AC%E5%B8%82%7C%E6%9C%9D%E9%98%B3%E5%8C%BA&lang=chs&region=CN"
    page = 1

    start_urls = [pre+str(page)+suf]

    def parse(self, response):
        print("response.url==",response.url)
        # print("response.text==", response.text)
        #str 类型json数据--->python对象的dict
        json_text = response.text
        #转换为字典了
        python_dict = json.loads(json_text)
        for item in python_dict["body"]["result"]:
            #创建item
            letvItem = LetvItem()
            #得到昵称
            nick = item.get("nick")
            #得到图片
            image = item.get("screenshot")

            #封装LetvItem
            letvItem["nick"] = nick
            letvItem["image"] = image
            # print("letvItem===", letvItem)
            yield letvItem


        #下一页
        if python_dict.get("header").get("status") == "1":
            self.page += 1
        #有可能这个链接有相同，但是爬虫不会重复去请求，发现所以的请求都已经完成，爬虫结束
        new_url = self.pre + str(self.page) + self.suf
        yield scrapy.Request(new_url,callback=self.parse)




