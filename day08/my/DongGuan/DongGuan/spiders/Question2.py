# -*- coding: utf-8 -*-
import scrapy

from DongGuan.items import DongguanItem


class Question2Spider(scrapy.Spider):
    name = 'Question2'
    allowed_domains = ['wz.sun0769.com']
    offset = 0
    url = 'http://wz.sun0769.com/index.php/question/questionType?type=4&page=0'
    start_urls = [url+str(offset)]


    def process_item(self,response):
        item = DongguanItem()
        url = response.url
        title_num = response.xpath('//div[@class="pagecenter p3"]//strong/text()').extract()

        title = title_num[0].split('\xa0\xa0')[0]
        title = title.split('：')[1]
        # print(title)
        number = title_num[0].split('\xa0\xa0')[1]
        number = number.split(':')[1]
        # print(number)
        content = response.xpath('//div[@class="c1 text14_2"]/text() | //div[@class="contentext"]/text()').extract()
        content = ''.join(content).strip()
        # print(content)
        item['url'] = url
        item['title'] = title
        item['number'] = number
        item['content'] = content
        yield item

    def parse(self, response):
        current_page_link = response.xpath('//a[@class="news14"]/@href').extract()
        for link in current_page_link:
            yield scrapy.Request(link, callback=self.process_item)
        if self.offset < 93671:
            self.offset += 30
        new_ulr = self.url+str(self.offset)
        yield scrapy.Request(new_ulr,callback=self.parse)
