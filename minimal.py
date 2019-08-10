import scrapy


class MinimalSpider(scrapy.Spider):
    """A menor Scrapy-Aranha do mundo!"""
    name = 'minimal'

    def start_requests(self):
        return [scrapy.Request(url) for url in['http://www.google.com', 'http://www.yahoo.com']]

    def parse(self, reponse):
        self.log('Acessando URL: %s' % response.url)
