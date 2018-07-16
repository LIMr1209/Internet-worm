# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.loader import ItemLoader
from Meizitu.items import MeizituItem


class MeinvtuSpider(scrapy.Spider):
    name = 'meinvtu'
    allowed_domains = ['meizitu.com']
    page = 1
    url = "http://www.meizitu.com/a/more_" + str(page) + ".html"
    start_urls = [url]

    def parse_detail(self, response):
        url = response.url
        item = ItemLoader(item=MeizituItem(), response=response)
        item.add_xpath("title", "//h2/a/text()")
        item.add_xpath("image_urls", '//div[@id="picture"]//img/@src')
        item.add_value('url', url)
        return item.load_item()

    def parse(self, response):
        urls = response.xpath('//div[@class="pic"]/a/@href').extract()
        print(urls)
        for url in urls:
            yield scrapy.Request(url, callback=self.parse_detail)

        if self.page < 72:
            self.page += 1

        url = "http://www.meizitu.com/a/more_" + str(self.page) + ".html"
        yield scrapy.Request(url, callback=self.parse)
