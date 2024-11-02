import scrapy
from scrapy.http import HtmlResponse
from scrapy.loader import ItemLoader
from itemloaders.processors import MapCompose
from ..items import ImgparserItem
import csv

__all__ = ['UnsplashcomSpider']

class UnsplashcomSpider(scrapy.Spider):
    name = "unsplashcom"
    allowed_domains = ["unsplash.com"]
    

    def __init__(self, **kwargs ):
        super().__init__(**kwargs)
        self.start_urls = [f"https://unsplash.com/s/photos/{kwargs.get('query')}"]


    def parse(self, response:HtmlResponse):
        # links = response.xpath('//img[@class="I7OuT DVW3V L1BOa"]').getall()
        links = response.xpath('//a[@class="zNNw1"]/@href').getall()
        # pass
        # //a[@class="vGXaw uoMSP kXLw7 R6ToQ qmXDq p4uUk kXLw7"] - author
        # //img[@class="I7OuT DVW3V L1BOa"]
        for link in links:
            yield response.follow(link, callback=self.unsplash_parse)
        print()

    def unsplash_parse(self, response:HtmlResponse):
        loader = ItemLoader(item=ImgparserItem(), response=response)
        loader.default_input_processor = MapCompose(str.strip)
        
        name = response.xpath("//h1[@class='vev3s']/text()").get()
        # name = response.xpath('//h1/text()').get()
        loader.add_value('name', name)

        category = response.xpath('//a[@class="m7tXD jhw7y TYpvC"]/text()').getall()
        loader.add_value('category', category)

        image_urls = response.xpath("//img[@class='I7OuT DVW3V L1BOa']/@srcset").getall()[0].split("?")[0]
        loader.add_value('image_urls', image_urls)

        yield loader.load_item()

        with open('./photos.csv', 'a', newline='', encoding='utf8') as f:
            writer = csv.writer(f)
            writer.writerow([name, category, image_urls])

        
