# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieDataItem(scrapy.Item):
    url = scrapy.Field()
    name = scrapy.Field()
    genre = scrapy.Field()
    country = scrapy.Field()
    duration = scrapy.Field()
    promotion = scrapy.Field()
    style = scrapy.Field()
    audience = scrapy.Field()
    story = scrapy.Field()
    time = scrapy.Field()
    key = scrapy.Field()
    watched = scrapy.Field()