# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

#继承scrapy.Item
class MyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    #姓名
    name = scrapy.Field()
    #简介
    info = scrapy.Field()
    #老师的图片
    image = scrapy.Field()
