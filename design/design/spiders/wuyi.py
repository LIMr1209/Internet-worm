import scrapy
from design.items import DesignItem
import json

data = {
    'channel': 'wuyi',
    'evt': 3,
    'company': '深圳市白狐工业设计有限公司'
}


class DesignCaseSpider(scrapy.Spider):
    name = 'wuyi'
    allowed_domains = ['www.woodesigncn.com']
    start_urls = ['http://www.woodesigncn.com/product.html']

    def parse(self, response):
        detail_list = response.xpath('//a[@data-toggle]/@href').extract()
        for i in detail_list:
            yield scrapy.Request('http://www.woodesigncn.com'+i, callback=self.parse_detail)

    def parse_detail(self, response):
        item = DesignItem()
        url = response.url
        img_url = response.xpath('//ul[@id="banner-list"]/li[1]/img/@src').extract()[0]
        if not img_url.startswith('http'):
            img_url = 'http://www.woodesigncn.com'+img_url
        remark = response.xpath('//div[@class="content"]//text()').extract()
        remark = [''.join(i.split()) for i in remark]
        remark = ''.join(remark)
        if len(remark) > 500:
            remark = remark[:500]
        title = response.xpath('//h4/text()').extract()[0]
        item['title'] = title
        item['remark'] = remark
        item['img_url'] = img_url
        item['url'] = url
        for key, value in data.items():
            item[key] = value
        # print(item)
        yield item
