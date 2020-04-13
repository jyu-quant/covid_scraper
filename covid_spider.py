import scrapy
from covid.items import CovidItem

class Covid_Spider(scrapy.Spider):
	name = "covid"

	def start_requests(self):
		yield scrapy.Request (url = 'https://www.worldometers.info/coronavirus/#countries',
							  callback = self.parse)

	def parse(self,response):
		item = CovidItem()
		item['country'] = response.css('a.mt_a::text').extract()
		item['total_cases'] = response.xpath('//*[@id="main_table_countries_today"]//tbody[1]//tr/td[2]/text()').extract()
		yield item