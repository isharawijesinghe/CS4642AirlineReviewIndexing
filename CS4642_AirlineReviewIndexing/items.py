# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Cs4642AirlinereviewindexingItem(scrapy.Item):

    name = scrapy.Field()
    review_from = scrapy.Field()
    review_date = scrapy.Field()
    trvelling_class = scrapy.Field()
    overall_rating = scrapy.Field()
    value_for_money_rating = scrapy.Field()
    seat_and_cabing_space_rating = scrapy.Field()
    customer_service_rating = scrapy.Field()
    entertainment_in_flight_rating = scrapy.Field()
    meal_and_beverage_rating = scrapy.Field()
    recomended = scrapy.Field()
    comment = scrapy.Field()
