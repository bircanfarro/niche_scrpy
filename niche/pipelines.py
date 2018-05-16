# -*- coding: utf-8 -*-

from scrapy.exporters import CsvItemExporter
from niche.items import EntityItem, FactItem, GradeItem, BadgeItem


FILENAME_ENTITIES = 'niche_entities.csv'
FILENAME_FACTS = 'niche_facts.csv'
FILENAME_GRADES = 'niche_grades.csv'
FILENAME_BADGES = 'niche_badges.csv'


class NicheItemPipeline(object):

	def open_spider(self, spider):
		self.entFile = open(FILENAME_ENTITIES, 'wb')
		self.entExporter = CsvItemExporter(self.entFile)
		self.entExporter.start_exporting()

		self.factFile = open(FILENAME_FACTS, 'wb')
		self.factExporter = CsvItemExporter(self.factFile)
		self.factExporter.start_exporting()

		self.grdFile = open(FILENAME_GRADES, 'wb')
		self.grdExporter = CsvItemExporter(self.grdFile)
		self.grdExporter.start_exporting()

		self.bdgFile = open(FILENAME_BADGES, 'wb')
		self.bdgExporter = CsvItemExporter(self.bdgFile)
		self.bdgExporter.start_exporting()


	def close_spider(self, spider):
		self.entExporter.finish_exporting()
		self.entFile.close()

		self.factExporter.finish_exporting()
		self.factFile.close()

		self.grdExporter.finish_exporting()
		self.grdFile.close()

		self.bdgExporter.finish_exporting()
		self.bdgFile.close()


	def process_item(self, item, spider):
		if isinstance(item, EntityItem):
			self.entExporter.export_item(item)
		elif isinstance(item, FactItem):
			self.factExporter.export_item(item)
		elif isinstance(item, GradeItem):
			self.grdExporter.export_item(item)
		elif isinstance(item, BadgeItem):
			self.bdgExporter.export_item(item)
		return item





