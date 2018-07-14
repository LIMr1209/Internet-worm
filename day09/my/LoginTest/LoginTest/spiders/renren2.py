# -*- coding: utf-8 -*-
import scrapy
import os

class Renren2Spider(scrapy.Spider):
    name = 'renren2'
    allowed_domains = ['renren.com']
    start_urls = ['http://www.renren.com/']

    def parse(self, response):
        yield scrapy.FormRequest.from_response(
            response,
            formdata={"email": os.environ.get('email'), "password": os.environ.get('password')},
            callback=self.login_success
        )

    def login_success(self, response):
        url = 'http://www.renren.com/881820831/profile'
        yield scrapy.Request(url, callback=self.save_page)

    def save_page(self, response):
        with open('郑爽.html', 'w', encoding='utf-8') as f:
            f.write(response.text)
