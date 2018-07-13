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
    #图片的链接
    image = scrapy.Field()
    #图片下载下来的保存位置
    image_path = scrapy.Field()
