# -*- coding: utf-8 -*-
import scrapy
import json

from lagou.items import CrawlersItem


class LagouSpider(scrapy.Spider):
    name = 'Lagou'
    allowed_domains = ['lagou.com']
    start_urls = ['https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=']
    pn = 1

    def parse(self, response):
        yield scrapy.FormRequest(
            url='https://www.lagou.com/jobs/positionAjax.json?city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false',
            formdata={'first': 'false', 'pn': str(self.pn), 'kd': 'python'},
            callback=self.parse_detail
        )

    def parse_detail(self, response):
        text = json.loads(response.text)
        res = []
        try:
            res = text["content"]["positionResult"]["result"]
            print(res)
        except:
            pass
        for position in res:
            item = CrawlersItem()
            try:
                item['title'] = position['positionName']
                item['education'] = position['education']
                item['company'] = position['companyFullName']
                item['experience'] = position['workYear']
                item['location'] = position['city']
                item['salary'] = position['salary']
            except:
                pass
            yield item
        self.pn += 1
        if self.pn<30:
            url = "https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false"
            formdata = {"kd": "python", "pn": str(self.pn), "first": "false"}
            yield scrapy.FormRequest(url, callback=self.parse_detail, formdata=formdata)

