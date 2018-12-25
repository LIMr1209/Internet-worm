import scrapy
from design.items import DesignItem
import json

data = {
    'channel': 'a-four',
    'evt': 3,
    'company': ' AFdesign.岸峰（上海）设计咨询有限公司'
}


class DesignCaseSpider(scrapy.Spider):
    name = 'a-four'
    allowed_domains = ['www.a-fourdesign.com']
    url = 'http://www.a-fourdesign.com/design_work.html'
    start_urls = [url]

    def parse(self, response):
        detail_list = response.xpath('//div[@class="d_case_list"]/ul[@class="clearfix"]/li')
        for i in detail_list:
            item = DesignItem()
            title = i.xpath('.//div[@class="h3"]/text()').extract()[0]
            tags = '工业设计,' + i.xpath('.//div[@class="p"]/text()').extract()[0]
            url = 'http://www.a-fourdesign.com' + i.xpath('./a/@href').extract()[0]
            item['url'] = url
            item['tags'] = tags
            item['title'] = title
            yield scrapy.Request(url, callback=self.parse_detail, meta={'item': item})

    def parse_detail(self, response):
        item = response.meta['item']
        img_url = response.xpath('//div[@class="d_case_info_banner"]//img/@src').extract()[0]
        if not img_url.startswith('http://www.a-fourdesign.com'):
            img_url = 'http://www.a-fourdesign.com'+img_url
        remark = response.xpath('//div[@class="d_case_info_banner"]//div[@class="p"]/text()').extract()[0]
        print(remark)
        item['remark'] = remark
        item['img_url'] = img_url
        for key, value in data.items():
            item[key] = value
        yield item
