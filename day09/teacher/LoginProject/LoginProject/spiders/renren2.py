# -*- coding: utf-8 -*-
import scrapy


class Renren2Spider(scrapy.Spider):
    name = 'renren2'
    allowed_domains = ['renren.com']
    start_urls = ['http://www.renren.com/']

    def parse(self, response):

        yield scrapy.FormRequest.from_response(
            #把首页的数据传入
            response,
            #请求成功后回调的方法
            callback=self.login_ok,
            formdata={"email": "yangguangfu2017@163.com", "password": "afu123456"}
        )


    #登录成功回调
    def login_ok(self,response):
        print("登录成功的数据到这里来")
        print("response.url==",response.url)
        with open("阿福哥.html", "w", encoding="utf-8") as f:
            f.write(response.text)

        url = "http://www.renren.com/881820831/profile"
        yield scrapy.Request(url,callback=self.save_zhengshua)


    #保存页面
    def save_zhengshua(self,response):

        with open("郑爽.html","w",encoding="utf-8") as f:
            f.write(response.text)
