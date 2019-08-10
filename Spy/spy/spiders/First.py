import scrapy


class FirstSpider(scrapy.Spider):
    name = 'first'
    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'https://www.ifood.com.br/lista-restaurantes'
        ]

        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):
        page = response.url.split('/')[-2]
        filename = 'first-%s.txt' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
