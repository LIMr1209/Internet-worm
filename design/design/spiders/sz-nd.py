import scrapy
from design.items import DesignItem
import json

data = {
    'channel': 'sz-nd',
    'evt': 3,
    'company': '深圳市无限空间工业设计有限公司'
}


class DesignCaseSpider(scrapy.Spider):
    name = 'sz-nd'
    allowed_domains = ['www.sz-nd.com']
    url = 'http://www.sz-nd.com/case.asp'
    start_urls = [url]

    def parse(self, response):
        category_list = response.xpath('//ul[@class="topnav"]/li[3]/ul/li/a/@href').extract()
        category_list.pop(0)
        category_list.pop(0)
        for i in category_list:
            yield scrapy.Request('http://www.sz-nd.com/'+i, callback=self.parse_category)
    def parse_category(self,response):
        detail_list = response.xpath('//div[contains(@class,"casebox")]')
        tags = response.xpath('//h2[1]/text()').extract()[0]
        detail_list.pop()
        for i in detail_list:
            try:
                url = i.xpath('./a/@href').extract()[0]
            except:
                return
            title = i.xpath('./div/h5/text()').extract()[0]
            yield scrapy.Request('http://www.sz-nd.com/'+url, callback=self.parse_detail,meta={'tags':tags,'title':title})
    def parse_detail(self, response):
        item = DesignItem()
        url = response.url
        tags = response.meta.get('tags')
        img_url = response.xpath('//div[@class="slide"]/img/@src').extract()[0]
        if not img_url.startswith('http'):
            img_url = 'http://www.sz-nd.com'+img_url
        try:
            remark = response.xpath('//div[@class="left"]/p[2]/text()').extract()[0]
        except:
            remark = ''
        title = response.meta.get('title')
        item['title'] = title
        item['remark'] = remark
        item['img_url'] = img_url
        item['url'] = url
        item['tags'] = tags
        for key, value in data.items():
            item[key] = value
        # print(item)
        yield item
