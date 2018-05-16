# -*- coding: utf-8 -*-
from scrapy import Spider, Request
from pprint import pprint
import json
from niche.items import EntityItem, FactItem, GradeItem, BadgeItem

MAX_PAGE = 99999
# MAX_PAGE = 2

PLACE_TYPES = (
	'best-places',
	'healthiest-places',
	'best-outdoors-places',
	'best-places-for-families',
	'safest-places',
	'best-public-schools-places',
	'most-diverse-places',
	'best-places-for-young-professionals',
	'best-places-to-retire',
	'cost-of-living-places',
	'best-places-to-buy-a-house',
)

def get_url(listURL, page):
	return 'https://www.niche.com/api/renaissance/results/?listURL=%s&page=%s&searchType=place' % (listURL, page)

class NicheJsonSpiderSpider(Spider):
	name = 'niche_json_spider'
	allowed_domains = ['niche.com']
	start_urls = [get_url(listURL, 1) for listURL in PLACE_TYPES]

	def parse(self, response):
		pprint(response)
		data = json.loads(response.text)

		for entity in data["entities"]:
			if 'guid' not in entity or 'name' not in entity or 'url' not in entity:
				continue
			item = EntityItem()
			item['entityGuid'] = entity['guid']
			item['name'] = entity['name']
			item['type_'] = entity.get('type')
			item['url'] = entity['url']
			item['tagline'] = entity.get('tagline')
			item['isClaimed'] = entity.get('isClaimed')
			item['isPremium'] = entity.get('isPremium')
			item['reviewCount'] = entity['reviewAverage'].get('count')
			item['reviewAverage'] = entity['reviewAverage'].get('average')
			yield item

			badge = entity.get('badge', {})
			if 'vanityURL' in badge and 'ordinal' in badge and 'total' in badge:
				item = BadgeItem()
				item['entityGuid'] = entity['guid']
				item['badgeType'] = badge['vanityURL']
				item['ordinal'] = badge['ordinal']
				item['total'] = badge['total']
				yield item


			for fact in entity["facts"]:
				if 'value' not in fact or 'label' not in fact:
					continue
				item = FactItem()
				item['entityGuid'] = entity['guid']
				item['label'] = fact['label']
				item['value'] = fact['value']
				yield item


			for grade in entity["grades"]:
				if 'value' not in grade or 'guid' not in grade or 'label' not in grade:
					continue
				item = GradeItem()
				item['entityGuid'] = entity['guid']
				item['guid'] = grade['guid']
				item['label'] = grade['label']
				item['value'] = grade['value']
				item['rankingGuid'] = grade.get('rankingGuid')
				yield item


		print('current page', data['page'])
		print('num entities:', len(data['entities']))
		page = data['page']
		if page >= MAX_PAGE or len(data['entities']) == 0:
			return
		yield Request(url=get_url(data['currentTopic']['listURL'], page + 1))










