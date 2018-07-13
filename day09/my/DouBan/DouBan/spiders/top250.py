# -*- coding: utf-8 -*-
import scrapy
from DouBan.items import DoubanItem


class Top250Spider(scrapy.Spider):
    name = 'top250'
    allowed_domains = ['douban.com']
    offset = 0
    url = 'https://movie.douban.com/top250?start='
    start_urls = [url + str(offset)]

    def parse(self, response):
        item = DoubanItem()
        movies = response.xpath('//div[@class="info"]')
        for movie in movies:
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
        if self.offset < 225:
            self.offset += 25
        next_url = self.url + str(self.offset)
        yield scrapy.Request(next_url, callback=self.parse)
