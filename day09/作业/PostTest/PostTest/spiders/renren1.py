# -*- coding: utf-8 -*-
import scrapy
import os

class Renren1Spider(scrapy.Spider):
    name = 'renren1'
    # allowed_domains = ['renren.com']
    # start_urls = ['http://renren.com/']
    url = 'http://www.renren.com/PLogin.do'

    def start_requests(self):
        yield scrapy.FormRequest(
            url=self.url,
            formdata={"email": os.environ.get('email'), "password": os.environ.get('password')},
            callback=self.parse
        )

    def parse(self, response):
        print(response.text)
