# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyDeepinBbsItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    forum_plate = scrapy.Field()
    autor_name = scrapy.Field()
    post_date = scrapy.Field()
    last_reply_name = scrapy.Field()
    last_reply_time = scrapy.Field()
    reply_num = scrapy.Field()
    pass
