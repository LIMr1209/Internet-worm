# -*- coding: utf-8 -*-
import scrapy
import json


#创建出来的爬虫，继承了Spider
from MySpider.items import MyspiderItem


class AtguiguSpider(scrapy.Spider):
    #爬虫名称
    name = 'Atguigu'
    #爬取的链接，要在些域名之内
    allowed_domains = ['www.atguigu.com']
    start_urls = ('http://www.atguigu.com/teacher.shtml',)

    #请求回来的数据，就通过该方法response返回回来
    #1.parse里面解析数据，用yield返回给pipelines
    #2.如果有的新的请求，添加到引擎里面
    def parse(self, response):
        print("response.url==",response.url)
        # print("response.body==",response.body)
        # print(type(response.body))
        # print("response.text===",response.text)

        node_list = response.xpath('//div[@class="teacher_content"]')

        # tearchs = []

        for node in node_list:

            #类似字典
            item = MyspiderItem()
            #.extract()作用转成utf-8编码
            # name = node.xpath('./p/text()|./div[@class="weibo"]/div[@class="l"]/text()').extract()
            #老师的姓名
            name = node.xpath('./p/text()|./div[@class="weibo"]/div[@class="l"]/text()').get()

            #老师的简介
            info =  node.xpath('./text()').extract()
            info = "".join(info).strip()


            #老师的图片,在返回的列表中第0下标有内容的，可以用get
            image = node.xpath('./img/@src').extract()[0]

            print("image===========================", image)

            item["name"] = name
            item["info"] = info
            item["image"] = image

            #以后返回数据，都用yield
            yield item

            # tearchs.append(item)

            # print(image)


        # #保存数据
        # f = open("teachers.json","w")
		  #
        # json.dump(tearchs,f,ensure_ascii=False)

