# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from Tencent.items import TencentItem


class Tencentposition2Spider(CrawlSpider):
    name = 'tencentPosition2'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['https://hr.tencent.com/position.php?&start=0']

    rules = (
        # 第一个参数,1:对该页面链接对象过滤的条件 2：如果不写如allow=r''，则请求该页面所有的链接
        # 第二个参数 1，请求成功后，回调的函数名
        # 第三个参数 True 表示请求过后的页面是否继续对该页面链接对象过滤请求爬取(深度)，False 表示只对该页面链接对象过滤请求爬取
        Rule(LinkExtractor(allow=r'start=\d+'), callback='parse_item', follow=True),
    )

    # 对于规则爬虫不能重写parse方法
    def parse_item(self, response):
        position_list = response.xpath('//tr[@class="even"] | //tr[@class="odd"]')
        for position in position_list:
            item = TencentItem()
            position_name = position.xpath("./td[1]/a/text()").get()
            position_link = position.xpath("./td[1]/a/@href").get()
            position_type = position.xpath("./td[2]/text()").extract()[0]
            people_num = position.xpath("./td[3]/text()").extract()[0]
            work_address = position.xpath("./td[4]/text()").get()
            publish_time = position.xpath("./td[5]/text()").get()
            item["position_name"] = position_name
            item["position_link"] = position_link
            item["position_type"] = position_type
            item["people_num"] = people_num
            item["work_address"] = work_address
            item["publish_time"] = publish_time

            yield item
