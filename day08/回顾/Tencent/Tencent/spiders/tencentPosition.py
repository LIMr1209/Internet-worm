# -*- coding: utf-8 -*-
import scrapy
from Tencent.items import TencentItem


class TencentpositionSpider(scrapy.Spider):
    name = 'tencentPosition'
    allowed_domains = ['hr.tencent.com']
    offset = 0
    url = 'https://hr.tencent.com/position.php?&start='
    start_urls = [url + str(offset)]

    def parse(self, response):
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
        total = response.xpath('//tr[@class="f"]//span/text()').extract()[0]
        if self.offset < int(total):
            self.offset += 10
        new_url = 'https://hr.tencent.com/position.php?&start=' + str(self.offset)
        yield scrapy.Request(new_url, callback=self.parse)
