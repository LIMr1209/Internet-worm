# -*- coding: utf-8 -*-
import scrapy


class RenrenSpider(scrapy.Spider):
    name = 'renren'
    # allowed_domains = ['renren.com']
    # start_urls = ['http://renren.com/']


    def start_requests(self):
        #请求的url,post请求
        url = "http://www.renren.com/PLogin.do"
        #scrapy提供post类
        yield scrapy.FormRequest(
            url=url,
            #请求成功后的回调
            callback=self.parse,
            #往服务器提交的数据
            formdata={"email":"yangguangfu2017@163.com","password":"afu123456"}
        )


    def parse(self, response):
        print("response.url==",response.url)
        print("response.text==",response.text)
        with open("阿福.html","w",encoding="utf-8") as f:
            f.write(response.text)
