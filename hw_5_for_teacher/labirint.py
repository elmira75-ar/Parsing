import urllib.parse
import scrapy
from scrapy.http import HtmlResponse
import urllib
from bookparser.items import BookparserItem
import csv


class LabirintSpider(scrapy.Spider):
    name = "labirint"
    allowed_domains = ["labirint.ru"]
    start_urls = ["https://www.labirint.ru/genres/2794/"]

    def parse(self, response:HtmlResponse):
        
        # print(response.status, response.url)
        # //a[@class="product-title-link"]/@href
        links = response.xpath('//a[@class="product-title-link"]/@href').getall()
        # print(links)
        # abs_links = [join('https://www.labirint.ru', link) for link in links]\
        for link in links:
            yield response.follow(link, callback=self.books_parse)
        
        next_page = response.xpath('//a[@class="pagination-next__text"]/@href').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
        # pass

    def books_parse(self, response:HtmlResponse):
        name = response.xpath('//h1/text()').get()
        price = response.xpath('//span[@class="buying-pricenew-val-number"]/text()').get()
        weight = response.xpath('//div[@class="weight"]/text()').get()
        yield BookparserItem(name=name, price=price, weight=weight)

        with open('./books_lab.csv', 'a', newline='', encoding='utf8') as f:
            writer = csv.writer(f)
            writer.writerow([name, price, weight])

        

