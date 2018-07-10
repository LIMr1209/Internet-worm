# -*- coding: utf-8 -*-
import scrapy


class AtguiguSpider(scrapy.Spider):
    #爬虫的名称，在该项目中唯一
    name = 'Atguigu'
    #允许的范围
    allowed_domains = ['www.atguigu.com']
    #爬虫开始爬取的起始url
    start_urls = ['http://www.atguigu.com/teacher.shtml']

    #请求数据成功后，会回调该方法
    def parse(self, response):
        print(response.url)
        #解码
        print(response.body.decode("utf-8"))

        with open("atgugiu_teacher.html","w") as f:
            f.write(response.body.decode("utf-8"))
