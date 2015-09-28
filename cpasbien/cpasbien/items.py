# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CpasbienItem(scrapy.Item):
    name = scrapy.Field()
    link = scrapy.Field()
    seeders = scrapy.Field()
    leechers = scrapy.Field()
    size = scrapy.Field()
    season = scrapy.Field()
    episode = scrapy.Field()
    quality = scrapy.Field()
    category = scrapy.Field()
