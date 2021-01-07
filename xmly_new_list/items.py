# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class XmlyNewListItem(scrapy.Item):
    # define the fields for your item here like:
    contentId = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    discountedPrice = scrapy.Field()
    priceTypeId = scrapy.Field()
    isPaid = scrapy.Field()
    customerTitle = scrapy.Field()
    playCount = scrapy.Field()
    cover = scrapy.Field()
    saleTypeId = scrapy.Field()
    albumType = scrapy.Field()
    hasPermission = scrapy.Field()
    expireTime = scrapy.Field()
    isSubscribed = scrapy.Field()
    supportVipDiscount = scrapy.Field()
