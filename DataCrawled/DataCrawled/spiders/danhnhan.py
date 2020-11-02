import scrapy 
from DataCrawled.items import DatacrawledItem

class QuotesSpider(scrapy.Spider):
	name = "danhnhan"
	start_urls=[
		'https://nguoikesu.com/dong-lich-su'
	]
	def parse(self, response):
		festivals= response.xpath('//*[@class="jm-module  title-star-ms"]/div/div/ul/li/a/@href').extract()

		for link in festivals:
#			print(link)
			yield scrapy.Request('https://nguoikesu.com'+link, callback=self.saveFile)
	def saveFile(self,response):
		name = response.xpath('//*[@itemprop="name"]/a/text()').extract()
#		print(name)
#		print(len(name))
	

#		print(name)
		for i in range(len(name)):
			content = response.xpath('//*[@class="leading-{}"]/p/text()'.format(i)).extract()
			
			if content is not None:
				strName = name[i].replace('\n','').replace('\t','');
				strContent=''.join(content)
#			link = response.url.encode("utf-8")
##
				nameFile = strName+'.txt'
				text = strContent.replace('\n','').replace('\t','').encode('utf-8')
				f = open('F:/Education/20201/Project III/Celebrity/DataCrawled/DataCrawled/DanhNhan/'+nameFile,'wb')
				f.write(text)
				f.close()

			#ghi link cac le hoi
				# nameFileLink = 'linkLeHoiWiki.txt'
				# f = open(nameFileLink,'ab+')
				# f.write(strName.encode('utf-8'))
				# f.write('\t'.encode('utf-8'))
				# f.write(link)
				# f.write('\n'.encode('utf-8'))
				# f.close()