# -*- coding: utf-8 -*-
import scrapy

from Dongguan.items import DongguanItem


class Question2Spider(scrapy.Spider):
    name = 'Question2'
    # allowed_domains = ['wz.sun0769.com']
    #偏移
    offset = 0
    url = "http://wz.sun0769.com/index.php/question/questionType?type=4&page="
    start_urls = [url+str(offset)]

    # start_urls = ["http://192.168.28.84:8080/index.html"]

    #就是帖子具体的内容了
    def process_item(self,response):
        item = DongguanItem()

        # 帖子链接
        url = response.url

        title_number = response.xpath('//div[@class="pagecenter p3"]/div/div/div/strong/text()').extract()

        if len(title_number) > 0:
            title_number = title_number[0]
            # 编号:191166
            # 帖子的编号
            number = title_number.split("\xa0\xa0")[1]
            number = number.split(":")[1]

            # 帖子标题
            title = title_number.split("\xa0\xa0")[0]
            title = title.split("：")[1]

            item["title"] = title
            item["number"] = number

        content = response.xpath('//div[@class="c1 text14_2"]/text()|//div[@class="contentext"]/text()').extract()
        # 把列表使用“”链接变成字符串
        content = "".join(content).strip()

        # print(content)

        item["url"] = url
        item["content"] = content

        yield item


    def parse(self, response):
        print("response.url===",response.url)


        #得到某一页的所以的帖子的链接
        current_page_link = response.xpath('//a[@class="news14"]/@href').extract()
        print(current_page_link)
        for link in current_page_link:
            #添加具体的帖子链接，让其帮我请求
            yield scrapy.Request(link,callback=self.process_item)


        #拼接下一页

        if self.offset < 93630:
           self.offset +=30
        #下一页的链接
        new_url = self.url+str(self.offset)
        yield scrapy.Request(new_url,callback=self.parse)
