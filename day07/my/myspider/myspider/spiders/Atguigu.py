# -*- coding: utf-8 -*-
import scrapy

from myspider.items import AtguiguItem


class AtguiguSpider(scrapy.Spider):
    name = 'Atguigu'
    allowed_domains = ['www.atguigu.com']
    start_urls = ["http://www.atguigu.com/teacher.shtml"]

    def parse(self, response):
        # filename = 'teacher.html'
        # content = response.body.decode()
        # with open(filename,'w',encoding='utf-8') as f:
        #     f.write(content)
        # teacher_items = []
        teacher_list = response.xpath('//div[@class="teacher_content"]')
        for teacher in teacher_list:

            item = AtguiguItem()
            # name1 = teacher.xpath("./div/div/text()").extract()
            # name2 = teacher.xpath("./p/text()").extract()
            # info = teacher.xpath('./text()').extract()[2].strip()
            # image = teacher.xpath('./img/@src').extract()[0]
            name = teacher.xpath('./div/div/text()|./p/text()').get()
            # get() 方法 相当与 .extract()[0]


            # 老师的简介
            info = teacher.xpath('./text()').extract()
            info = "".join(info).strip()

            # 老师的图片
            image = teacher.xpath('./img/@src').get()
            # if name1:
            #     name = name1[0]
            # else:
            #     name = name2[0]
            item['name'] = name
            item['info'] = info
            item['image'] = image
            # teacher_items.append(item)
            # print(item)
        # return teacher_items
            yield item






