# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Meizitu2Item(scrapy.Item):
    # define the fields for your item here like:
    #帖子的链接
    url = scrapy.Field()
    #帖子的标题
    tilte = scrapy.Field()
    #图片的链接列表
    image_urls = scrapy.Field()
    #图片保存到本地的列表
    image_paths = scrapy.Field()

