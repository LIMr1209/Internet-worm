# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LetvItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    nick = scrapy.Field()
    image = scrapy.Field()
    image_path =scrapy.Field()
