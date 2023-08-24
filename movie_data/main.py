from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from docs.mongo_crawl import clearDb
from docs.mongo_find import MongoConnectionFinder
import argparse
import datetime
from os import system
current_time = datetime.datetime.now()
print(f"{current_time.hour}:{current_time.minute}")

def finder():
    process = CrawlerProcess(get_project_settings())
    process.crawl('finder')
    process.start()
    process.join()
def crawler():
    process = CrawlerProcess(get_project_settings())
    process.crawl('crawler')
    process.start()
    process.join()
    
def check():
    system('py docs/check.py')

def clear():
    clearDb()
    con = MongoConnectionFinder()
    con.clearDb()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="crawl helper", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', action='store_true', help='finder')
    parser.add_argument('-x', action='store_true', help='crawler')
    parser.add_argument('-c', action='store_true', help='checker')
    parser.add_argument('-l', action='store_true', help='delete')
    args = parser.parse_args()
    config = vars(args)
    find = config['f']
    checker = config['c']
    crawl = config['x']
    dele = config['l'] 
    if find:
        finder()         
    elif checker:
        check()
    elif crawl:
        crawler()
    elif dele:
        clear()        
