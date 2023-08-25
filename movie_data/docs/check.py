from mongo_find import MongoConnectionFinder
from mongo_crawl import MongoConnectionCrawler

def check():
    connectionone_one = MongoConnectionFinder()
    connectionone_one.clearDb()
    connection_two = MongoConnectionCrawler()
    connection_two.clearDb()
    connection_one = MongoConnectionFinder()
    connection_two = MongoConnectionFinder()
    urls = connection_two.find_all()
    read = 0
    more = 0
    for url in urls:
        read += 1
        number = urls.count(url)
        if number > 1:
            print(f"Error -{number}-> {url}")
            more += 1
    print(f"\nCRAWLED:\nCOUNTED --> {read}\nMORE --> {more}")
    urls = connection_one.find_all()
    read = 0
    more = 0
    for url in urls:
        read += 1
        number = urls.count(url)
        if number > 1:
            print(f"Error -{number}-> {url}")
            more += 1
    print(f"\nMOVIES:\nCOUNTED --> {read}\nMORE --> {more}")