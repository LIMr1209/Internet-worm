import scrapy
from design.items import DesignItem
import json

data = {
    'channel': 'bfit',
    'evt': 3,
    'company': '上海柏菲工业产品设计有限公司'
}


class DesignCaseSpider(scrapy.Spider):
    name = 'bfit'
    allowed_domains = ['www.bfitdesign.com']
    category = {'22': '科学仪器', '23': '医疗器械设计', '24': '工业设备', '25': '消费电子', '26': '家用电器', '27': '文化产品','37':'其他行业'}
    category_list = ['22', '23', '24', '25', '26', '27','37']
    category_index = 0
    url = 'http://www.bfitdesign.com/case'+category_list[category_index]+'-1.aspx'
    start_urls = [url]


    def parse(self, response):
        detail_list = response.xpath('//li[@class="caselistitem"]/a/@href').extract()
        for i in detail_list:
            yield scrapy.Request('http://www.bfitdesign.com/'+i, callback=self.parse_detail)

        if self.category_index < 6:
            self.category_index += 1
            yield scrapy.Request(url ='http://www.bfitdesign.com/case'+self.category_list[self.category_index]+'-1.aspx',callback=self.parse)

    def parse_detail(self, response):
        item = DesignItem()
        url = response.url
        tags = ''
        if self.category[self.category_list[self.category_index]] != '其他行业':
            tags = self.category[self.category_list[self.category_index]]

        img_url = response.xpath('//ul[@class="pic"]/li/img/@src').extract()[0]
        if not img_url.startswith('http'):
            img_url = 'http://www.bfitdesign.com/'+img_url
        title = response.xpath('//*[@class="p2"]/text()').extract()[0]
        item['title'] = title
        item['img_url'] = img_url
        item['url'] = url
        item['tags'] = tags
        for key, value in data.items():
            item[key] = value
        yield item
