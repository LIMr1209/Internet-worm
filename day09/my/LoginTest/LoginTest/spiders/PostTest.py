# -*- coding: utf-8 -*-
import scrapy


class PosttestSpider(scrapy.Spider):
    name = 'PostTest'
    # allowed_domains = ['httpbin.org']
    # start_urls = ['http://httpbin.org/']

    def start_requests(self):
        url = 'http://httpbin.org/post'
        #post请求
        yield scrapy.FormRequest(url=url, formdata={'name': '张三'}, callback=self.parse)

    def parse(self, response):
        print(response.url)
        print(response.body)   #bytes 类型的
        print(response.text)   #字符串类型的
