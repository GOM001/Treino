import scrapy


class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    star_urls = [
        'https://www.amazon.com.br/Celulares-Desbloqueados/b/?ie=UTF8&node=16243890011&ref_=sv_b_3']

    def parse(self, response):
        items = AmazonItem()
        product_name = response.css('h2.s-access-title::text').extract()
        product_price = response.css('span.sx-price-whole::text').extract()
        items['product_name'] = product_name
        items['product_price'] = product_price
        yield items
