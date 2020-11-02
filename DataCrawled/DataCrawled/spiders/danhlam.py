import scrapy 
from scrapy.selector import Selector
from DataCrawled.items import DatacrawledItem

class QuotesSpider(scrapy.Spider):
	name = "danhlam"
	start_urls=[
		'https://www.maxreading.com/sach-hay/danh-lam-thang-canh.html'
	]
	def parse(self, response):
		festivals= response.xpath('//tbody/tr/td/a/@href').extract()

		for link in festivals:
			link=link.replace("..",'');
#			print(link)
			yield scrapy.Request('https://www.maxreading.com'+link, callback=self.saveFile)

	def saveFile(self,response):
#		pass
		name = response.xpath('//h3/text()').extract()
#		print(name)
#		content = response.xpath('//*[@id="chapter"]/div/p/text()').extract()
		question = Selector(response).xpath('//*[@id="chapter"]/div')
		content = question.css('p ::text').getall()

		if content is not None:
			strName = name[0];
			strContent=''.join(content)
#			link = response.url.encode("utf-8")

			nameFile = strName+'.txt'
			text = strContent.replace("\xa0",'').replace("\xad",'').replace('         ','').encode("utf-8")
			f = open('F:/Education/20201/Project III/Celebrity/DataCrawled/DataCrawled/DanhLam/'+nameFile,'wb')
			f.write(text)
			f.close()
