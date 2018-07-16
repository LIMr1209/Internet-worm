# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MeizituItem(scrapy.Item):
    # define the fields for your item here like:
    #帖子链接
    url = scrapy.Field()
    #标题
    title = scrapy.Field()
    #图片链接
    image = scrapy.Field()
    #图片保存链接
    image_path = scrapy.Field()
