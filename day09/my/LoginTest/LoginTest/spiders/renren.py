# -*- coding: utf-8 -*-
import scrapy


class RenrenSpider(scrapy.Spider):
    name = 'renren'

    # allowed_domains = ['renren.com']
    # start_urls = ['http://www.renren.com/']

    def start_requests(self):
        yield scrapy.FormRequest(
            url='http://www.renren.com/PLogin.do',
            formdata={"email": "aaa1058169464@126.com", "password": "aaa1058169464"},
            callback=self.parse
        )

    def parse(self, response):

        print(response.text)