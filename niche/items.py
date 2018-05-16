# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class EntityItem(scrapy.Item):
	# define the fields for your item here like:
	entityGuid = scrapy.Field()
	name = scrapy.Field()
	type_ = scrapy.Field()
	url = scrapy.Field()
	tagline = scrapy.Field()
	isClaimed = scrapy.Field()
	isPremium = scrapy.Field()
	reviewCount = scrapy.Field()
	reviewAverage = scrapy.Field()

class FactItem(scrapy.Item):
	entityGuid = scrapy.Field()
	label = scrapy.Field()
	value = scrapy.Field()


class GradeItem(scrapy.Item):
	#overall niche grades
	entityGuid = scrapy.Field()
	guid = scrapy.Field()
	label = scrapy.Field()
	value = scrapy.Field()
	rankingGuid = scrapy.Field()

class BadgeItem(scrapy.Item):
	entityGuid = scrapy.Field()
	badgeType = scrapy.Field()
	ordinal = scrapy.Field()
	total = scrapy.Field()







