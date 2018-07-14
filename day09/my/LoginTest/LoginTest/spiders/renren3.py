# -*- coding: utf-8 -*-
import scrapy


class Renren3Spider(scrapy.Spider):
    name = 'renren3'
    allowed_domains = ['renren.com']
    start_urls = ['http://renren.com/']
    cookies = {
        "anonymid": "jj3le9ma9dv3ic",
        "_r01_": "1",
        "jebe_key": "d92a25c2-cc9f-4cc7-99c5-96c958035aCf%7C58980be99b0de10fe7adab87f46cb9D7%7C1530582242945%7C1%7C1530582247259",
        "ln_hurl": "http://head.xiaonei.com/photos/0/0/men_main.gif",
        "__utma": "151146938.465862207.1530582258.1530582258.1530618090.2",
        "__utmz": "151146938.1530618090.2.2.utmcsr=renren.com|utmccn=(referral)|utmcmd=referral|utmcct=/966762689/profile",
        "hm_lvt_966bff0a868cd407a416b4e3993b9dc8": "1530618290",
        "_ga": "GA1.2.465862207.1530582258",
        "depovince": "BJ",
        "jebecookies": "9c76139b-4870-44c6-a61a-f481726b1f8f|||||",
        "ick_login": "fb6b0501-180f-4617-9cc7-37d5f2d12c44",
        "_de": "043211665AC233F263D6383A089C903A016C1A0D299EDE5B",
        "p": "f93fa34c12db88f0085751d68fc6d28f9",
        "first_login_flag": "1",
        "ln_uact": "aaa1058169464@126.com",
        "t": "117085d8f7b6eac57d52af0ab74611fc9",
        "societyguester": "117085d8f7b6eac57d52af0ab74611fc9",
        "id": "966762689",
        "loginfrom": "syshome",
        "JSESSIONID": "AbcoDe1k3hg4vGr9gIrsw",
        "wp_fold": "0",
        "xnsid": "6e75a677",
        "XNESSESSIONID": "aBCMNAPAwVKJt7g7xJrsw",
    }

    def start_requests(self):
        yield scrapy.FormRequest(
            url=self.start_urls[0],
            cookies=self.cookies,
            callback=self.parse
        )

    def parse(self, response):
        print(response.text)
