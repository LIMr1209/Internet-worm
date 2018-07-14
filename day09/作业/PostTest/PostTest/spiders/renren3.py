# -*- coding: utf-8 -*-
import scrapy


class Renren3Spider(scrapy.Spider):
    name = 'renren3'
    # allowed_domains = ['renren.com']
    # start_urls = ['http://renren.com/']
    cookies = {
        "anonymid": "jjjz1wem-pfaxfv",
        "depovince": "SX",
        "_r01_": "1",
        "ick_login": "c031d1e9-a535-4deb-a0dd-efe4dcbfc7c4",
        "_de": "043211665AC233F263D6383A089C903A016C1A0D299EDE5B",
        "p": "08a30b57e80ecd2e6840cf06b9d2821d9",
        "first_login_flag": "1",
        "ln_uact": "aaa1058169464@126.com",
        "ln_hurl": "http://head.xiaonei.com/photos/0/0/men_main.gif",
        "t": "9ab7a8481dc62cd2c2f2f384180587de9",
        "societyguester": "9ab7a8481dc62cd2c2f2f384180587de9",
        "id": "966762689",
        "xnsid": "6c56563d",
        "loginfrom": "syshome",
        "jebecookies": "dde4df58-1b6a-4424-8f5f-7f17d29e9475|||||",
        "JSESSIONID": "ABCTByiGHiqTEEw2dQtsw",
        "wp_fold": "0",
    }

    def start_requests(self):
        yield scrapy.FormRequest(
            url='http://renren.com/',
            cookies=self.cookies,
            callback=self.parse
        )

    def parse(self, response):
        print(response.text)
