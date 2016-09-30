# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LdsHymnScraperItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    number = scrapy.Field()
    music = scrapy.Field()
    text = scrapy.Field()
    scriptures = scrapy.Field()
    meter = scrapy.Field()
    topic = scrapy.Field()
    tune = scrapy.Field()
