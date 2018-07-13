# -*- coding: utf-8 -*-
import scrapy
import re

from DongGuan.items import DongguanItem


class Question2Spider(scrapy.Spider):
    name = 'Question2'
    allowed_domains = ['wz.sun0769.com']
    offset = 0
    url = 'http://wz.sun0769.com/index.php/question/questionType?type=4&page='
    start_urls = [url + str(offset)]

    def parse_item(self, response):
        item = DongguanItem()
        url = response.url
        title_num = response.xpath('//div[@class="pagecenter p3"]//strong/text()').extract()[0]
        title = title_num.split('  ')[0]
        title = title.split('：')[1]
        num = title_num.split('  ')[1]
        num = num.split(':')[1]
        content = response.xpath(
            '//div[@class="content text14_2"]/div[@class="c1 text14_2"]/text() | //div[@class="contentext"]/text()').extract()
        content = ''.join(content).strip()
        item['url'] = url
        item['title'] = title
        item['num'] = num
        item['content'] = content
        yield item

    def parse(self, response):
        content_detail_links = response.xpath('//a[@class="news14"]/@href').extract()
        for link in content_detail_links:
            yield scrapy.Request(link, callback=self.parse_item)
        num_total = response.xpath('//div[@class="pagination"]/text()').extract()
        num_total = re.compile('\d+').search(num_total[len(num_total) - 1]).group()
        if self.offset < int(num_total):
            self.offset += 30

        new_url = self.url + str(self.offset)
        yield scrapy.Request(new_url, callback=self.parse)
