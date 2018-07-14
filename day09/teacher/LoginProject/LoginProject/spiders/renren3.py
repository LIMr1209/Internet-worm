# -*- coding: utf-8 -*-
import scrapy


class Renren3Spider(scrapy.Spider):
    name = 'renren3'
    # allowed_domains = ['renren.com']
    # start_urls = ['http://renren.com/']

    cookies = {
        "anonymid": "jj4dweuc8urouu",
        "_r01_": "1",
        "ln_uact": "yangguangfu2017@163.com",
        "ln_hurl": "http://hdn.xnimg.cn/photos/hdn421/20180312/1720/h_main_rI1p_b6d2000d171a1986.jpg",
        "depovince": "ZGQT",
        "jebe_key": "64445fd6-45d2-4f9d-8c6c-0569db5effda%7C23d7f054f633e4326590e7719a77981f%7C1530543234521%7C1%7C1531406529681",
        "JSESSIONID": "abclx-hWrkB1C6jqjBrsw",
        "ick_login": "f323b054-52d0-454a-b4bc-4e9244451e94",
        "first_login_flag": "1",
        "wp_fold": "0",
        "jebecookies": "918972a4-266f-4edb-a270-e2a7ffad0697|||||",
        "_de": "839AB3C91139E616062ACF0F25D1AE7D5BF7EAB63017E04A",
        "p": "7eae2f4f1c8cdb48b3ae73a5708174c50",
        "t": "45b060a3a5c5b395df64329099ece8540",
        "societyguester": "45b060a3a5c5b395df64329099ece8540",
        "id": "964604530",
        "xnsid": "6e8876bf",
        "ver": "7.0",
        "loginfrom": "null",


    }
    def start_requests(self):
        # 请求的url,post请求
        url = "http://www.renren.com/881820831/profile"
        # scrapy提供post类
        yield scrapy.FormRequest(
            url=url,
            # 请求成功后的回调
            callback=self.parse,
            # 往服务器提交的数据
            cookies=self.cookies
        )

    def parse(self, response):
        with open("郑爽.html", "w", encoding="utf-8") as f:
            f.write(response.text)
