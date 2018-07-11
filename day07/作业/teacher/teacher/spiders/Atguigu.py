# -*- coding: utf-8 -*-
import scrapy
from teacher.items import TeacherItem

class AtguiguSpider(scrapy.Spider):
    name = 'Atguigu'
    allowed_domains = ['guigu.com']
    start_urls = ['http://www.atguigu.com/teacher.shtml']

    def parse(self, response):
        teacher_list = response.xpath('//div[@class="teacher_content"]')
        for teacher in teacher_list:
            item = TeacherItem()
            name = teacher.xpath('./div/div/text()|./p/text()').extract()[0]
            info = teacher.xpath('./text()').extract()
            info = ''.join(info).strip()
            image = teacher.xpath('./img/@src').get()
            item['name'] = name
            item['info'] = info
            item['image'] = image
            yield item
            