# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ImdbItem(scrapy.Item):
    # define the fields for your item here like:
    id = scrapy.Field()
    Title = scrapy.Field()
    # genere = scrapy.Field()
    Avg_rating = scrapy.Field()
    total_ratings = scrapy.Field()
    user_reviews = scrapy.Field()
    critic_reviews = scrapy.Field()
    description = scrapy.Field()
    # certificate = scrapy.Field()
    # release_date = scrapy.Field()
    # runtime = scrapy.Field()
    # sound_mix = scrapy.Field()
    Avg_rating = scrapy.Field()
    total_ratings = scrapy.Field()
    Country_of_origin = scrapy.Field()
    Aspect_ratio = scrapy.Field()
    Sound_mix = scrapy.Field()
    Runtime = scrapy.Field()
    Budget = scrapy.Field()
    Production_companies = scrapy.Field()
    Language = scrapy.Field()
    Release_date = scrapy.Field()
    Certificate = scrapy.Field()
    Genres = scrapy.Field()
    Writer = scrapy.Field()
    Director = scrapy.Field()
    Stars = scrapy.Field()
