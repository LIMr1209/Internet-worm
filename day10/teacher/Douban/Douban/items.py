# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    #影片的标题
    tilte = scrapy.Field()

    #影片的信息
    content = scrapy.Field()
    #影片的评分
    score = scrapy.Field()
    #影片的一语句后简介
    info = scrapy.Field()
