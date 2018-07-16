# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MysinaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    parent_title = scrapy.Field()
    parent_url = scrapy.Field()
    sub_title = scrapy.Field()
    sub_url = scrapy.Field()
    sub_file_name = scrapy.Field()
    son_url = scrapy.Field()
    head = scrapy.Field()
    content = scrapy.Field()
    son_path = scrapy.Field()