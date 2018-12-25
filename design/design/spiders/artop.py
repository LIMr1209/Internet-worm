import scrapy
from design.items import DesignItem
import json
import re
data = {
    'channel': 'artop',
    'evt': 3,
    'company': '上海浪尖工业设计有限公司'
}


class DesignCaseSpider(scrapy.Spider):
    name = 'artop'
    allowed_domains = ['www.artop-sh.com']
    category = {'2cf03': '智能科技', '01e9b': '家居家电', '65962': '交通出行', '7e2c0': '机器人', '147e1': '机械自动化', '27ff8': '健康医疗','55fe6':'设计研究','99efd':'其他'}
    category_list = ['2cf03', '01e9b', '65962', '7e2c0', '147e1', '27ff8','55fe6','99efd']
    url = 'http://www.artop-sh.com/industrial#_case'
    start_urls = [url]


    def parse(self, response):
        for j in self.category_list:
            x = '//div[@class="row list-show"]/a[contains(@class,"%s")]' %j
            detail_list = response.xpath(x)
            for i in detail_list:
                item = DesignItem()
                url = 'http://www.artop-sh.com'+i.xpath('./@href').extract()[0]
                tags = self.category[j]
                title = i.xpath('./p/text()').extract()[0]
                img_url = i.xpath('./span/i/@data-src').extract()[0]
                if not img_url.startswith('http'):
                    img_url = 'http://www.artop-sh.com' + img_url
                item['title'] = title
                item['img_url'] = img_url
                item['url'] = url
                item['tags'] = tags
                for key, value in data.items():
                    item[key] = value
                yield scrapy.Request(url=url,callback=self.parse_detail,meta={"item":item})

    def parse_detail(self,response):
        item = response.meta['item']
        url = response.url
        item['url'] = url
        remark = response.xpath('//div[@class="padding-md"]//text()').extract()
        remark = [''.join(i.split()) for i in remark]
        remark = ''.join(remark).strip()
        if len(remark) > 480:
            remark = remark[:480]
        item['remark'] = remark

        yield item







