# -*- coding: utf-8 -*-
import scrapy
from Tencent.items import AtguiguItem

class TencentpositionSpider(scrapy.Spider):
    name = 'TencentPosition'
    allowed_domains = ['hr.tencent.com']
    #偏移量
    offset = 0#0,10,20,30,
    url = "https://hr.tencent.com/position.php?&start="
    start_urls = [url+str(offset)+"#a",]

    def parse(self, response):
        print("response.url==",response.url)
        # print("response.text==",response.text)
        postion_lists = response.xpath('//tr[@class="even"]|//tr[@class="odd"]')

        for postion in postion_lists:
            item = AtguiguItem()
            #.extract()作用：把节点转换成unicode编码
            postion_name = postion.xpath('./td[1]/a/text()').extract()[0]
            postion_link = postion.xpath('./td[1]/a/@href').extract()[0]
            postion_type = postion.xpath('./td[2]/text()').get()
            people_number = postion.xpath('./td[3]/text()').extract()[0]
            work_address = postion.xpath('./td[4]/text()').extract()[0]
            publish_time = postion.xpath('./td[5]/text()').extract()[0]

            # print(postion_name,postion_link,postion_type,people_number,work_address,publish_time)
            item["postion_name"] = postion_name
            item["postion_link"] = postion_link
            item["postion_type"] = postion_type
            item["people_number"] = people_number
            item["work_address"] = work_address
            item["publish_time"] = publish_time


            yield item


        #请求下一页
        total_page = response.xpath('//div[@class="left"]/span/text()').extract()[0]
        print("total_page===",total_page)

        if self.offset  < int(total_page):
            #每一页，相差10
            self.offset += 10

        #每一页的请求链接
        new_url = self.url+str(self.offset)+"#a"
        #往scrapy引擎添加请求
        yield scrapy.Request(new_url,callback=self.parse)






