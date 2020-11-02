import scrapy 
from DataCrawled.items import DatacrawledItem

class QuotesSpider(scrapy.Spider):
	name = "danhnhanmax"
	start_urls=[
		'https://www.maxreading.com/sach-hay/danh-nhan-nuoc-viet.html'
	]
	def parse(self, response):
		celebrity= response.xpath('//*[@id="content"]/div/div[1]/div/table/tbody/tr/td[2]/a/@href').extract()
		for link in celebrity:
			yield scrapy.Request(link.replace('..', 'https://www.maxreading.com'), callback=self.saveFile)

	def saveFile(self,response):
		name = response.xpath('//*[@id="content"]/div/div[1]/div/h3/text()').extract()
		content = response.xpath('string(//*[@id="chapter"]/p)').extract()
		# if content is not None:
		strName = ''.join(name)
		strContent = '|'.join(content)
		nameFile = strName.lstrip()+'.txt'
		text = strContent.replace('\n','').replace('|','').encode('utf-8')
		link = response.url.encode("utf-8")
		f = open('F:/Education/20201/Project III/Celebrity/DataCrawled/DataCrawled/DanhNhanMax/'+nameFile,'wb')
		f.write(text)
		f.close()
		#ghi link cac le hoi
		# nameFileLink = 'link76Lehoi.txt'
		# f = open(nameFileLink,'ab+')
		# f.write(strName.encode('utf-8'))
		# f.write('\t'.encode('utf-8'))
		# f.write(link)
		# f.write('\n'.encode('utf-8'))
		# f.close()
				
			