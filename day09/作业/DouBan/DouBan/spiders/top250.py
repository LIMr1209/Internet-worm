# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from DouBan.items import DoubanItem

class Top250Spider(CrawlSpider):
    name = 'top250'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/top250?start=0&filter=']

    rules = (
        Rule(LinkExtractor(allow=r'start=\d+&filter='), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        movies = response.xpath('//div[@class="info"]')
        for movie in movies:
            item = DoubanItem()
            title = movie.xpath('.//span[@class="title"][1]/text()').extract()[0]
            content = movie.xpath('.//div[@class="bd"]/p[1]/text()').extract()
            content = ''.join(content).strip().replace('\n', '')
            score = movie.xpath('.//div[@class="star"]/span[2]/text()').extract()[0]
            info = movie.xpath('.//span[@class="inq"]/text()').extract()
            if len(info) > 0:
                info = info[0]
            item["title"] = title
            item["content"] = content
            item["score"] = score
            item["info"] = info
            yield item


