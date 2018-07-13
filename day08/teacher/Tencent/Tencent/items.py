# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AtguiguItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #职位名称
    postion_name = scrapy.Field()
    #职位的链接
    postion_link = scrapy.Field()
    #职位类型
    postion_type = scrapy.Field()
    #招聘的人数
    people_number = scrapy.Field()
    #工作地点
    work_address = scrapy.Field()
    #发布时间
    publish_time = scrapy.Field()
