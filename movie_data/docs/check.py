from mongo_find import MongoConnectionFinder
from mongo_crawl import find_all, clearDb

def check():
    connection = MongoConnectionFinder()
    urls = find_all()
    read = 0
    more = 0
    for url in urls:
        read += 1
        number = urls.count(url)
        if number > 1:
            print(f"Error -{number}-> {url}")
            more += 1
    print(f"\nCRAWLED:\nCOUNTED --> {read}\nMORE --> {more}")
    urls = connection.find_all()
    read = 0
    more = 0
    for url in urls:
        read += 1
        number = urls.count(url)
        if number > 1:
            print(f"Error -{number}-> {url}")
            more += 1
    print(f"\nMOVIES:\nCOUNTED --> {read}\nMORE --> {more}")

def clear():
    connection = MongoConnectionFinder()
    connection.clearDb()
    clearDb()


# clear()
check()