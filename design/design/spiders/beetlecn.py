import scrapy
from design.items import DesignItem
import json

data = {
    'channel': 'beetlecn',
    'evt': 3,
    'company': '广州百拓设计有限公司'
}


class DesignCaseSpider(scrapy.Spider):
    name = 'beetlecn'
    allowed_domains = ['www.beetlecn.com']
    start_urls = ['http://www.beetlecn.com/sort.php']
    def parse(self, response):
        category_list = response.xpath('//*[@id="ul"]/li/a/@href').extract()
        for i in category_list:
            yield scrapy.Request('http://www.beetlecn.com/'+i, callback=self.parse_category)


    def parse_category(self, response):
        detail_list = response.xpath('//*[@id="Li"]/li[position()>1]/a/@href').extract()
        for i in detail_list:
            yield scrapy.Request('http://www.beetlecn.com/'+i,callback=self.parse_detail)

    def parse_detail(self, response):
        item = DesignItem()
        img_url = response.xpath('//div[@class="pro_right"]/img/@src').extract()[0]
        if not img_url.startswith('http'):
            img_url = 'http://www.beetlecn.com/'+img_url
        url = response.url
        tags = response.xpath('//div[@class="pro_left"]/span[1]/text()').extract()[0]
        tags = tags.split('> > ')[1]
        title = response.xpath('//div[@class="pro_left"]/p/text()').extract()[0]
        if title == '广告小图':
            return
        try:
            remark = response.xpath('//div[@class="pro_left"]/span[2]/text()').extract()[0]
        except:
            remark = ''
        item['remark'] = remark
        item['title'] = title
        item['img_url'] = img_url
        item['url'] = url
        item['tags'] = tags
        for key, value in data.items():
            item[key] = value
        # print(tags,self.page)
        yield item
