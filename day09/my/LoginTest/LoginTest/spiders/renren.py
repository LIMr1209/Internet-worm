# -*- coding: utf-8 -*-
import scrapy


class RenrenSpider(scrapy.Spider):
    name = 'renren'

    # allowed_domains = ['renren.com']
    # start_urls = ['http://www.renren.com/']

    def start_requests(self):
        yield scrapy.FormRequest(
            url='http://www.renren.com/PLogin.do',
            formdata={"email": os.environ.get('email'), "password": os.environ.get('password')},
            callback=self.parse
        )

    def parse(self, response):

        print(response.text)