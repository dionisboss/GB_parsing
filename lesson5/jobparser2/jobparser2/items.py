# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Jobparser2Item(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    salary = scrapy.Field()
    _id = scrapy.Field()
    experience=scrapy.Field()
    type_of_work = scrapy.Field() #full or part time
    vac_text =scrapy.Field()
    key_skills = scrapy.Field()
    company = scrapy.Field()
