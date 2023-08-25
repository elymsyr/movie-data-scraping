from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
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

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="crawl helper", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', action='store_true', help='finder')
    parser.add_argument('-x', action='store_true', help='crawler')
    parser.add_argument('-c', action='store_true', help='checker')
    args = parser.parse_args()
    config = vars(args)
    find = config['f']
    checker = config['c']
    crawl = config['x']
    if find:
        finder()         
    elif checker:
        check()
    elif crawl:
        crawler()     
