import scrapy
from design.items import DesignItem
import json

data = {
    'channel': 'idform',
    'evt': 3,
    'company': '深圳艾德方设计有限公司'
}


class DesignCaseSpider(scrapy.Spider):
    name = 'idform'
    allowed_domains = ['www.idform.cn']
    page = 1
    url = 'http://www.idform.cn/design_case/'
    start_urls = [url]

    def parse(self, response):
        detail_list = response.xpath('//div[@class="list"]/a/@href').extract()
        for i in detail_list:
            yield scrapy.Request('http://www.idform.cn/design_case/' + i, callback=self.parse_detail)
        if self.page < 5:
            self.page += 1
            yield scrapy.Request('http://www.idform.cn/design_case/design_case_' + str(self.page) + '.html')

    def parse_detail(self, response):
        item = DesignItem()
        url = response.url
        tags = response.xpath('//ol[@class="breadcrumb"]/li[position()>2]//text()').extract()
        tags = ','.join(tags)
        img_url = response.xpath('//ul[@id="lightgallery"]/li/img/@src').extract()[0]
        if not img_url.startswith('http'):
            img_url = 'http://www.idform.cn/include/thumb.php?dir=' + img_url
        title = response.xpath('//h1[@class="met_title"]/text()').extract()[0]
        item['title'] = title
        item['img_url'] = img_url
        item['url'] = url
        item['tags'] = tags
        for key, value in data.items():
            item[key] = value
        # print(item)
        yield item
