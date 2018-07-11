# -*- coding: utf-8 -*-
import scrapy
import json
from letv.items import LetvItem


class LetvinfoSpider(scrapy.Spider):
    name = 'letvinfo'
    allowed_domains = ['letv.com']
    page = 1
    pre = 'http://dynamic.live.app.m.letv.com/android/dynamic.php?luamod=main&mod=live&ctl=liveHuya&act=channelList&pcode=010210000&version=7.17&channelId=2168&pages='
    suf = '&country=CN&provinceid=1&districtid=9&citylevel=1&location=%E5%8C%97%E4%BA%AC%E5%B8%82%7C%E6%9C%9D%E9%98%B3%E5%8C%BA&lang=chs&region=CN'
    url = pre + str(page) + suf
    start_urls = [url]

    def parse(self, response):
        json_obj = response.body
        python_dict = json.loads(json_obj)
        for item in python_dict["body"]["result"]:
            letvitem = LetvItem()
            nick = item.get("nick")
            image = item.get("screenshot")
            letvitem["nick"] = nick
            letvitem["image"] = image
            yield letvitem
        if python_dict.get('header').get('status') == 1:
            self.page += 1
        new_url = self.pre + str(self.page) + self.suf
        yield scrapy.Request(new_url, callback=self.parse)
