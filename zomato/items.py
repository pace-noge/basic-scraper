# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZomatoItem(scrapy.Item):
    name = scrapy.Field()
    area = scrapy.Field()
    address = scrapy.Field()
    cuisine_type = scrapy.Field()
    cuisine_region = scrapy.Field()
    price = scrapy.Field()
    rating = scrapy.Field()
     