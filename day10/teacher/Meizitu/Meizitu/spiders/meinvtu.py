# -*- coding: utf-8 -*-
import scrapy

from Meizitu.items import MeizituItem


class MeinvtuSpider(scrapy.Spider):
    name = 'meinvtu'
    allowed_domains = ['mm131.com']
    page = 2

    url = "http://www.mm131.com/xinggan/list_6_"+str(page)+".html"

    start_urls = [url]

    def parse_detail(self,response):
        # print("response.url===",response.url)
        #好多的图片
        images = response.xpath("//img/@src").extract()
        title = response.xpath("//h5/text()").extract()[0]
        for image in images:

            item = MeizituItem()
            item["image"] = image
            item["title"] = title
            item["url"] = response.url
            yield item






    def parse(self, response):
        # print("response.url===",response.url)
        #得到某页面的所以的帖子的url
        links = response.xpath("//dd/a/@href").extract()

        for link in links:
            print("link====================",link)
            if link.endswith(".html"):
                yield scrapy.Request(link,callback=self.parse_detail)

