# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LetvItem(scrapy.Item):
    # define the fields for your item here like:
    #昵称
    nick = scrapy.Field()
    #直播的封面,对应的字段screenshot
    image = scrapy.Field()
    #存储保存图片的位置(本地)
    image_path = scrapy.Field()
