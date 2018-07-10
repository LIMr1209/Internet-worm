# -*- coding: utf-8 -*-
import scrapy


class AtguiguSpider(scrapy.Spider):
    name = 'Atguigu'
    allowed_domains = ['www.atguigu.com']
    start_urls = ["http://www.atguigu.com/teacher.shtml", ]

    def parse(self, response):
        # filename = "teacher.html"
        # open(filename, 'w',encoding='utf-8').write(response.body.decode('utf-8'))
        teacher_list = response.xpath('//div[@class="teacher_content"]')
        teacher_items = []
        for teacher in teacher_list:
            item = {}
            name1 = teacher.xpath('./div/div/text()').extract()
            name2 = teacher.xpath('./p/text()').extract()
            infos = teacher.xpath('./text()').extract()
            images = teacher.xpath('./img/@src').extract()
            if len(name1) > 0:
                name = name1[0]
            else:
                name = name2[0]
            info = infos[2].strip()
            image = images[0]
            item['name'] = name
            item['info'] = info
            item['image'] = image
            print(item)
            teacher_items.append(item)
        return teacher_items
