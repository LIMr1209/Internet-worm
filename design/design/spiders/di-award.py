# -*- coding: utf-8 -*-
import scrapy
from design.items import DesignItem


data = {
    'channel': 'di-award',
    'evt': 3,
    'prize_id': 18,
    'prize': '中国设计制造大奖',
}


class ChinagoodSpider(scrapy.Spider):
    name = 'di-award'
    year = 2018  # 2017,2016
    level_1 = 1  # 1智造奖2设计义乌3设计先临
    level_2 = 1  # 1.1 金智奖 1.2 优智奖 1.3创智奖 1.4 智造奖   2.1 一等奖 2.2 二等奖 2.3 三等奖 2.4 设计先乌  3.1 一等奖 3.2 二等奖 3.3 三等奖 3.4 设计先临
    url = 'http://www.di-award.org/exhibition/s/y/%s/t/%s/a/%s.html' %(year,level_1,level_2)

    start_urls = [url]

    def parse(self, response):
        detail_list = response.xpath('//ul[@class="list"]/li/a[1]/@href').extract()
        for i in detail_list:
            yield scrapy.Request(url=i,callback=self.parse_detail,dont_filter=True)
        if self.level_2 < 4:
            self.level_2 += 1
            level2_url = 'http://www.di-award.org/exhibition/s/y/%s/t/%s/a/%s.html' %(self.year,self.level_1,self.level_2)
            yield scrapy.Request(url=level2_url,callback=self.parse,dont_filter=True)
        else:
            if self.level_1 < 3:
                self.level_2 = 1
                self.level_1 += 1
                level1_url = 'http://www.di-award.org/exhibition/s/y/%s/t/%s/a/%s.html' %(self.year,self.level_1,self.level_2)
                yield scrapy.Request(url=level1_url,callback=self.parse,dont_filter=True)
            else:
                if self.year > 2016:
                    self.year -= 1
                    self.level_2 = 1
                    self.level_1 = 1
                    year_url = 'http://www.di-award.org/exhibition/s/y/%s/t/%s/a/%s.html' %(self.year,self.level_1,self.level_2)
                    yield scrapy.Request(url=year_url,callback=self.parse,dont_filter=True)


    def parse_detail(self,response):
        item = DesignItem()
        prize_level = response.xpath('//ul[@class="eparams"]/li[1]/text()').extract()[1].strip()
        prize_time = self.year
        url = response.url
        img_url = response.xpath('//div[@class="eimglist"]/a[1]/img/@src').extract()[0]
        img_url = img_url.replace('c200x200','a768')
        if not img_url.startswith('http'):
            img_url = 'http://cdn.di-award.org' + img_url
        remark = response.xpath('//p[@class="econtent"]//text()').extract()
        remark = [''.join(i.split()) for i in remark]
        remark = ''.join(remark)
        title = response.xpath('//h3/text()').extract()[0]
        company = response.xpath('//ul[@class="eparams"]/li[2]/text()').extract()[1].strip()
        if len(remark) > 480:
            remark = remark[:480]
        item['title'] = title
        item['remark'] = remark
        item['url'] = url
        item['img_url'] = img_url
        item['company'] = company
        item['prize_level'] = prize_level
        item['prize_time'] = prize_time
        for key, value in data.items():
            item[key] = value
        # print(item)
        yield item

