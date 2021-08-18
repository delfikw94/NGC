import scrapy


class SpiderimdbSpider(scrapy.Spider):
    name = 'spiderimdb'
    allowed_domains = ['https://www.imdb.com/search/title/?genres=animation']
    start_urls = ['http://https://www.imdb.com/search/title/?genres=animation/']

    def parse(self, response):
        judul = response.xpath('//h3[@class="lister-item-header"]/a/text()').extract()
        rating = response.xpath('//div[@class="inline-block ratings-imdb-rating"]/strong/text()').extract()
        deskripsi = response.xpath('//p[@class="text-muted"]/text()').extract()
        votes = response.xpath('//p[@class="sort-num_votes-visible"]/span/text()').extract()
        poster = response.xpath('//img[@class="loadlate"]/@src').extract()

        for item in zip(judul, rating, deskripsi, votes, poster):
            
            scraped_data = {
                'Judul': item[0],
                'Rating': item[1],
                'Deskripsi': item[2],
                'Votes': item[3],
                'Poster': item[4]
            }
            yield scraped_data