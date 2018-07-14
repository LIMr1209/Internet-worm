# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

#规则爬虫，继承CrawlSpider
from Tencent.items import AtguiguItem


class Tencentposition2Spider(CrawlSpider):
    #爬虫名称
    name = 'TencentPosition2'
    #允许爬取范围
    allowed_domains = ['hr.tencent.com']

    start_urls = ['https://hr.tencent.com/position.php?&start=0']

    #reles规则，里面可以添加多个规则
    rules = (
        #Rule,
        # 第一参数：1.对链接对象过滤的条件；2.如果allow对应的正则是空，匹配所以链接,3.一般情况要写
        #第二个参数：1.使用正则匹配的链接，如果请求成功后，回调那个方法;2.如果这个回调不写可以吗
        #第三个参数：follow=True深度爬取,只要满足这个正则的所以链接都会去爬取，否则值爬取当前页面
        Rule(LinkExtractor(allow=r'start=\d'), callback='parse_item', follow=True),
    )

    #对应规则爬虫，一定不要重写parse，否则覆盖父类parse的方法
    #应为在父类的方法里面负责逻辑的调用
    # def parse(self, response):
    #     print("response.url==", response.url)
    #     # print("response.text==",response.text)


    def parse_item(self, response):
        print("response.url====",response.url)

        postion_lists = response.xpath('//tr[@class="even"]|//tr[@class="odd"]')

        for postion in postion_lists:
            item = AtguiguItem()
            # .extract()作用：把节点转换成unicode编码
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