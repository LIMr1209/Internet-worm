# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from mysina.items import MysinaItem


class Sina1Spider(CrawlSpider):
    name = 'sina1'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://sina.com.cn/']

    rules = (
        Rule(LinkExtractor(allow=r'http://\w+.sina.com.cn/\w+/')),
        Rule(LinkExtractor(allow=r'http://\w+.sina.com.cn/.+shtml'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = MysinaItem()
        item['son_url'] = response.url
        print(response.url)
        heads = response.xpath(
            '//h1[@class="main-title"]/text()|//div[@class="blkContainerSblk"]/h1[@id="artibodyTitle"]/text()|//div[@class="crticalcontent"]/h1/span/text()'
            '').extract()
        head = "".join(heads).strip()
        contents = response.xpath(
            '//div[@class="article"]/p/text()|//div[@id="artibody"]/p/text()|//div[@class="s_infor"]/p/text()').extract()
        content = ''.join(contents).strip()
        item['head'] = head
        item['content'] = content
        print(item)
        yield item
