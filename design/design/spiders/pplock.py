import scrapy
from design.items import DesignItem
import re

data = {
    'channel': 'pplock',
    'evt': 3,
}


class DesignCaseSpider(scrapy.Spider):
    name = 'pplock'
    allowed_domains = ['www.pplock.com']
    page = 1
    start_urls = ['http://www.pplock.com/industrial-design']

    def parse(self, response):
        detail_list = response.xpath('//div[@class="post"]')
        for i in detail_list:
            item = DesignItem()
            url = i.xpath('./div[1]/a/@href').extract()[0]
            title = i.xpath('./div[2]/h2//text()').extract()[0]
            img_url = i.xpath('./div[1]/a/img/@src').extract()[0]
            tags = i.xpath('.//div[@class="category"]//text()').extract()
            for i in range(tags.count(' ')):
                tags.remove(' ')
            for i in range(tags.count(', ')):
                tags.remove(', ')
            img_url = img_url.replace('-326x246', '')
            item['tags'] = tags
            item['img_url'] = img_url
            item['url'] = url
            item['title'] = title
            for key, value in data.items():
                item[key] = value

            yield scrapy.Request(url, callback=self.parse_detail, meta={'item': item})

        if self.page < 30:
            self.page += 1
            yield scrapy.Request(url='http://www.pplock.com/industrial-design/page/' + str(self.page),
                                 callback=self.parse)

    def parse_detail(self, response):
        item = response.meta['item']
        remark = response.xpath('//div[@class="post-content"]/p[position()<3]//text()').extract()
        remark = [''.join(i.split()) for i in remark]
        remark = ''.join(remark).strip()
        item['remark'] = remark
        print(item)
        yield item

