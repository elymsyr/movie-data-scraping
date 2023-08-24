import scrapy
from ..docs.mongo_find import MongoConnectionFinder
from ..docs.mongo_crawl import insert
from ..items import MovieDataItem
import re

# scrapy crawl crawler

class CrawlSpider(scrapy.Spider):
    name = "crawler"
    allowed_domains = ["tarzifilm.com"]
    connection = MongoConnectionFinder()
    start_urls = connection.find_to_crawl()
    print(f"Crawling {len(start_urls)}")

    def parse(self, response):
        item = MovieDataItem()
        clear_data = []
        data = self.clean_text((response.xpath('//div[@class="column-content-c"][1]').getall())[0]).strip()
        item['url'] = response.url
        item['name'] = ''
        item['genre'] = []
        item['country'] = []
        item['duration'] = ''
        item['promotion'] = ''
        item['style'] = []
        item['audience'] = []
        item['story'] = []
        item['time'] = []
        item['key'] = []
        item['watched'] = 0
        data = data.split('\n')
        for row in range(len(data)):
            data[row] = data[row].replace('\r', '')
            data[row] = data[row].replace('\n', '')
            data[row] = data[row].strip()
            if len(data[row]) == 0 or data[row].startswith('(adsbygoogle'):
                pass
            else:
                clear_data.append(data[row])
        for data in clear_data:
            number = clear_data.index(data)
            if data.startswith('Orjinal başlık: '):
                item['name'] = data.replace('Orjinal başlık: ', '')
            if data.startswith('Tür: '):
                item['genre'] = self.make_list(data.replace('Tür: ', ''))
            if data.startswith('Ülke: '):
                item['country'] = self.make_list(data.replace('Ülke: ', ''))
            if data.startswith('Süre: '):
                item['duration'] = data.replace('Süre: ', '')
            if data == 'Tanıtım:':
                item['promotion'] = clear_data[number+1]
            if data == 'Tarz:':
                item['style'] = self.make_list(clear_data[number+1])
            if data == 'Seyirci kitlesi:':
                item['audience'] = self.make_list(clear_data[number+1])
            if data == 'Hikaye:':
                item['story'] = self.make_list(clear_data[number+1])
            if data == 'Zaman:':
                item['time'] = self.make_list(clear_data[number+1])
            if data == 'Anahtar kelime:':
                item['key'] = self.make_list(clear_data[number+1])
        if item['name'] == '' or item['name'] == None:
            new_name = response.xpath('//div[@class="name-c"]/span').extract_first().strip()
            item['name'] = self.remove_html(new_name)
        data = [item['url'], item['name'], item['genre'], item['country'], item['duration'], item['promotion'], item['style'], item['audience'], item['story'], item['time'], item['key'], item['watched']]
        insert(data)
        self.connection.update_state(data[0][21:])
    
    def remove_html(self, string):
        regex = re.compile(r'<[^>]+>')
        return regex.sub('', string)
        
    def clean_text(self, raw_html):
        cleantext = re.sub(re.compile('<.*?>'), '', raw_html)
        return cleantext
    def make_list(self, item):
        if item == None or item == 'Tarz:' or item == 'Seyirci kitlesi:' or item == 'Hikaye:' or item == 'Zaman:' or item == 'Anahtar kelime:' or item == '' or item == []:
            return []
        else:
            item = item.replace('...', '').lower()
            item = item.split(',')
            for i in range(len(item)):
                item[i] = item[i].strip()
            return item