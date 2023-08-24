import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..docs.mongo_find import MongoConnectionFinder

# scrapy crawl finder

class FinderSpider(CrawlSpider):
    name = "finder"
    allowed_domains = ["tarzifilm.com"]
    connection = MongoConnectionFinder()
    connection.clearDb()
    urls = connection.find_all()
    urls.reverse()
    start_urls = urls
    print(f"\n\n\nSTARTING {len(start_urls)}")
    new = 0
    rules = (Rule(LinkExtractor(allow=r"benzer/", unique=True), callback="parse_item", follow=True),)

    def parse_item(self, response):
        movies = response.css('div.item-name')
        for movie in movies:
            data = str(movie.css('a.name::attr(href)').extract_first())
            if self.connection.check_exists(data):
                self.connection.insert(data)
                self.new += 1
                if self.new % 200 == 0:
                    print(f"Added --> {self.new}")
                    print(f"Total --> {self.new+len(self.start_urls)}")