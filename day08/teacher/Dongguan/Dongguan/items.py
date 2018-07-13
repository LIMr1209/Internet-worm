# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DongguanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 每个帖子的标题
    title = scrapy.Field()
    # 每个帖子的编号
    number = scrapy.Field()
    # 每个帖子的内容
    content = scrapy.Field()
    # 每个帖子的链接
    url = scrapy.Field()
