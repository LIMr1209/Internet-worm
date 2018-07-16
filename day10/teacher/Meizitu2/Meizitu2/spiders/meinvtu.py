# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.loader import ItemLoader

from Meizitu2.items import Meizitu2Item


class MeinvtuSpider(scrapy.Spider):
    name = 'meinvtu'
    allowed_domains = ['meizitu.com']
    page = 1
    url = "http://www.meizitu.com/a/more_"+str(page)+".html"
    start_urls = [url]

    def parse_detail(self,response):
        print("response.url===", response.url)
        #具体值
        url = response.url

        #使用ItemLoader类
        item = ItemLoader(item=Meizitu2Item(),response=response)
        item.add_xpath("tilte","//h2/a/text()")
        item.add_xpath("image_urls",'//div[@id="picture"]//img/@src')
        #添加值的方式
        item.add_value("url",url)

        return item.load_item()

        # pass

    def parse(self, response):
        # print("response.url===",response.url)
        #得到所以帖子的链接
        urls = response.xpath('//div[@class="pic"]/a/@href').extract()
        print(urls)
        for url in urls:
            # print("urls===",url)
            yield scrapy.Request(url,callback=self.parse_detail)


        if self.page < 72:
            self.page +=1

        url = "http://www.meizitu.com/a/more_" + str(self.page) + ".html"
        yield scrapy.Request(url,callback=self.parse)

