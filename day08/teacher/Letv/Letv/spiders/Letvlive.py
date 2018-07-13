# -*- coding: utf-8 -*-
import scrapy
import json
from Letv.items import LetvItem

#LetvliveSpider名字可以任意，继承scrapy.Spider,基本爬虫
class LetvliveSpider(scrapy.Spider):
    #爬虫名称，在当前项目中名字不能重复发
    name = 'Letvlive'
    #爬取的网站，只能在这个范围内容,如果注释掉，没有域名的限制，所以的网站都可以爬
    allowed_domains = ['letv.com']
    page = 1

    pre = "http://dynamic.live.app.m.letv.com/android/dynamic.php?luamod=main&mod=live&ctl=liveHuya&act=channelList&pcode=010210000&version=7.17&channelId=2168&pages="
    suf = "&country=CN&provinceid=1&districtid=9&citylevel=1&location=%E5%8C%97%E4%BA%AC%E5%B8%82%7C%E6%9C%9D%E9%98%B3%E5%8C%BA&lang=chs&region=CN"
    #start_urls里面的链接不受allowed_domains这里面的现在
    start_urls = [pre+str(page)+suf]

    def parse(self, response):
        print("response.url===",response.url)
        print("response.text====",response.text)

        # yield scrapy.Request("https://www.baidu.com/")

        #python -->str -->dict
        json_text = response.text

        #把json_text 转换成python_dict
        python_dict = json.loads(json_text)

        for item in python_dict["body"]["result"]:
            letvItem = LetvItem()
            #获取昵称
            nick = item["nick"]
            image = item["screenshot"]
            letvItem["nick"] = nick
            letvItem["image"] = image

            print(letvItem)
            #传递给pipelines（管道）
            yield letvItem

        if   python_dict.get("header").get("status")  == "1":
            self.page += 1

        new_url = self.pre + str(self.page) + self.suf

        #会有相同的url链接，这个链接请求了，就不去请求
        #把所以添加的链接，做去重处理，请求，当再次添加相同的链接进入的时候，判断请求过了，就不请求了
        #把添加的，没有重复的请求后，爬虫结束了

        yield scrapy.Request(new_url,callback=self.parse)




