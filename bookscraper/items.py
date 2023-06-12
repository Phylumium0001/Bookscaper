# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BookscraperItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    pass



class BookItem(scrapy.Item):
    url =         scrapy.Field()
    title =       scrapy.Field()
    category =    scrapy.Field()
    price =       scrapy.Field()
    price_w_tax = scrapy.Field()
    stock =       scrapy.Field()
    description = scrapy.Field()
    ratings =      scrapy.Field()