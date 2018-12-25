import scrapy
from design.items import DesignItem
import json

data = {
    'channel': 'daetu',
    'evt': 3,
    'company': '德腾工业设计有限公司'
}


class DesignCaseSpider(scrapy.Spider):
    name = 'daetu'
    allowed_domains = ['www.daetumdesign.com']
    start_urls = ['http://www.daetumdesign.com/?anli/Product3/']
    page = 1
    category = ['3','6','45','48','46','55','49','4','5','7','47']
    category_index = 0


    def parse(self, response):
        detail_list = response.xpath('//ul[@class="newUl clearfix"]/li/a/@href').extract()
        for i in detail_list:
            yield scrapy.Request('http://www.daetumdesign.com'+i, callback=self.parse_detail)
        page = response.xpath('//div[@class="page"]/ul/li[last()]//text()').extract()[0]
        if self.page < int(page):
            self.page += 1
            yield scrapy.Request('http://www.daetumdesign.com/?anli/Product'+self.category[self.category_index]+'/Index_'+str(self.page)+'.html',callback=self.parse)
        else:
            if self.category_index < 10:
                self.page = 1
                self.category_index += 1
                yield scrapy.Request('http://www.daetumdesign.com/?anli/Product'+self.category[self.category_index]+'/',callback=self.parse)


    def parse_detail(self, response):
        item = DesignItem()
        url = response.url
        tags = response.xpath('//*[@id="dqnav"]/a/text()').extract()[0][:-2]
        try:
            img_url = response.xpath('//*[@id="alst"]//img/@src').extract()[0]
        except:
            img_url = response.xpath('//*[@id="sjks"]//img/@src').extract()[0]
        if not img_url.startswith('http'):
            img_url = 'http://www.daetumdesign.com'+img_url
        title = response.xpath('//div[@class="infonav3"]/dl/dt/text()').extract()[0]
        title = title.replace('\r\n','').strip()
        item['title'] = title
        item['img_url'] = img_url
        item['url'] = url
        item['tags'] = tags

        for key, value in data.items():
            item[key] = value
        yield item
