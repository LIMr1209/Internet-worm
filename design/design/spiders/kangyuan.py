import scrapy
from design.items import DesignItem
import json

data = {
    'channel': 'kangyuan',
    'evt': 3,
    'company': '深圳市康源工业设计有限公司'
}


class DesignCaseSpider(scrapy.Spider):
    name = 'kangyuan'
    allowed_domains = ['www.yu-kangyuan.com']
    url = 'http://www.yu-kangyuan.com/Case.html'
    start_urls = [url]

    def parse(self, response):
        detail_list = response.xpath('//div[@class="workBox"]/a/@href').extract()
        for i in detail_list:
            yield scrapy.Request('http://www.yu-kangyuan.com' + i, callback=self.parse_detail)

    def parse_detail(self, response):
        item = DesignItem()
        url = response.url
        title = response.xpath('//div[@class="c_left"]/div/p[1]/b/text()').extract()[0]
        img_url = response.xpath('//div[@class="case_content"]//img/@src').extract()[0]
        if not img_url.startswith('http'):
            img_url = 'http://www.yu-kangyuan.com' + img_url
        item['title'] = title
        item['img_url'] = img_url
        item['url'] = url
        for key, value in data.items():
            item[key] = value
        yield item
