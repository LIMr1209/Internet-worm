# -*- coding: utf-8 -*-
import scrapy


#post请求,提交数据
class PosttestSpider(scrapy.Spider):
    name = 'posttest'
    # allowed_domains = ['httpbin.org']
    # start_urls = ['http://httpbin.org/']

    def start_requests(self):
        #请求的url,post请求
        url = "http://httpbin.org/post"
        #scrapy提供post类
        yield scrapy.FormRequest(
            url=url,
            #请求成功后的回调
            callback=self.parse,
            #往服务器提交的数据
            formdata={"name":"zhangsan","age":"18"}
        )



    def parse(self, response):
        print("response.url===",response.url)
        print("response.text===", response.text)
