# -*- coding: utf-8 -*-
import scrapy
from design.items import DesignItem

# 中国家具设计金点奖
data = {
    'channel': 'jiagle',
    'name': '',
    'color_tags':'',
    'brand_tags': '',
    'material_tags': '',
    'style_tags': '',
    'technique_tags': '',
    'other_tags': '',
    'user_id': 0,
    'kind': 1,
    'brand_id': 0,
    'prize_id': 22,
    'prize': '中国家具设计金点奖',
    'evt': 3,
    'prize_level': '',
    'prize_time': '',
    'category_id': 0,
    'status': 1,  # 状态
    'deleted': 0,  # 是否软删除
    'info': '',
}


class DesignCaseSpider(scrapy.Spider):
    name = 'jindian'
    allowed_domains = ['gida.jiagle.com']
    id = 2  # 2,3,4,5,6,7
    start_urls = ['http://gida.jiagle.com/match/' + str(id) + '.html']

    def parse(self, response):
        design_list = response.xpath('//li[contains(@class,"ft")]/a/@href').extract()
        tags = response.xpath('//li[@class="active"]/a/text()').extract()[0]
        for design in design_list:
            yield scrapy.Request(design, callback=self.parse_detail,
                                 meta={'tags': tags})
        if self.id < 7:
            self.id += 1
            yield scrapy.Request('http://gida.jiagle.com/match/' + str(self.id) + '.html', callback=self.parse)

    def parse_detail(self, response):
        url = response.url
        item = DesignItem()
        tags = response.meta['tags']
        img_url = response.xpath('//div[@id="productBig"]/img/@src').extract()[0]
        if img_url.endswith('.pdf'):
            return
        message = response.xpath('//div[@class="detail-title"]//dd/text()').extract()
        title = message[0]
        company = message[1]
        designer = message[2]
        remark = response.xpath('//div[@class="detail-text-box"]/p/text()').extract()[0]
        remark = remark.replace('\n','').replace(' ','').replace('\r','').strip()
        print(remark)
        item['url'] = url
        item['img_url'] = img_url.strip()
        item['title'] = title.strip()
        item['company'] = company.strip()
        item['remark'] = remark
        item['tags'] = tags
        item['designer'] = designer.strip()
        for key, value in data.items():
            item[key] = value
        yield item
