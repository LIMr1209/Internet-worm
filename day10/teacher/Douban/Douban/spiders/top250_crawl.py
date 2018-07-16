# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from Douban.items import DoubanItem


class Top250CrawlSpider(CrawlSpider):
    name = 'top250_crawl'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250?start=0&filter=']

    rules = (
        Rule(LinkExtractor(allow=r'start=\d+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        print("response.url================================", response.url)

        all_node = response.xpath('//div[@class="info"]')
        for node in all_node:

            item = DoubanItem()
            print("--" * 100)
            # 影片的标题
            tilte = node.xpath('.//span[@class="title"][1]/text()').extract()[0]
            # 影片的信息
            content = node.xpath('.//div[@class="bd"]/p/text()').extract()[0]
            # 影片的评分
            score = node.xpath('.//div[@class="star"]/span[2]/text()').extract()[0]
            # 影片的一句话简介
            info = node.xpath('.//p[@class="quote"]/span/text()').extract()
            if len(info) > 0:
                info = info[0]

            item["tilte"] = tilte
            item["content"] = content
            item["score"] = score
            item["info"] = info

            # print(item)

            yield item