# -*- coding: utf-8 -*-
import scrapy
from Meizitu.items import MeizituItem


class Meinvtu3Spider(scrapy.Spider):
    name = 'meinvtu3'
    allowed_domains = ['meizitu.com']
    page = 1
    url = "http://www.meizitu.com/a/more_" + str(page) + ".html"
    start_urls = [url]

    def parse(self, response):
        urls = response.xpath('//div[@class="pic"]/a/@href').extract()
        print(urls)
        for url in urls:
            yield scrapy.Request(url, callback=self.parse_detail)

        if self.page < 72:
            self.page += 1

        url = "http://www.meizitu.com/a/more_" + str(self.page) + ".html"
        yield scrapy.Request(url, callback=self.parse)

    def parse_detail(self, response):
        item = MeizituItem()
        title = response.xpath('//h2/a/text()').get()
        image_urls = response.xpath('//div[@id="picture"]//img/@src').extract()
        url = response.url
        item['title'] = title
        item['image_urls'] = image_urls
        item['url'] = url
        yield item
