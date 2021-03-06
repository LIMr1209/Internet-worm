# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from Meizitu.items import MeizituItem
from scrapy.loader import ItemLoader


class Meinvtu2Spider(CrawlSpider):
    name = 'meinvtu2'
    allowed_domains = ['meizitu.com']
    start_urls = ["http://www.meizitu.com/a/more_1.html"]

    rules = (
        Rule(LinkExtractor(allow=r'/a/more_\d.html/')),
        Rule(LinkExtractor(allow=r'/a/\d+.html'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        url = response.url
        item = ItemLoader(item=MeizituItem(), response=response)
        item.add_xpath('title', '//h2/a/text()')
        item.add_xpath('image_urls', '//div[@id="picture"]//img/@src')
        item.add_value('url', url)
        return item.load_item()
