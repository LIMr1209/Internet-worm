# -*- coding: utf-8 -*-
import scrapy
from DongGuan.items import DongguanItem


class Position2Spider(scrapy.Spider):
    name = 'Position2'
    allowed_domains = ['wz.sun0769.com']
    offset = 0
    url = 'http://wz.sun0769.com/index.php/question/questionType?type=4&page='
    start_urls = [url + str(offset)]

    def parse_item(self, response):
        item = DongguanItem()
        url = response.url
        title_num = response.xpath('//div[@class="pagecenter p3"]//strong[@class="tgray14"]/text()').extract()[0]
        title = title_num.split('  ')[0]
        title = title.split('：')[1]
        num = title_num.split('  ')[1]
        num = num.split(':')[1]
        content = response.xpath('//div[@class="c1 text14_2"]//text() | //div[@class="contentext"]/text()').extract()
        content = "".join(content).strip()
        item['title'] = title
        item['url'] = url
        item['num'] = num
        item['content'] = content
        return item

    def parse(self, response):
        all_links = response.xpath('//a[@class="news14"]/@href').extract()
        for link in all_links:
            yield scrapy.Request(link, callback=self.parse_item)
        if self.offset < 93737:
            self.offset += 30
        new_url = self.url + str(self.offset)
        yield scrapy.Request(new_url, callback=self.parse)
