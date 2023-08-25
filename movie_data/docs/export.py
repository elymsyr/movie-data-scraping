from pandas import DataFrame
from mongo_crawl import MongoConnectionCrawler

def mongo_export_to_file():
    connection = MongoConnectionCrawler()
    mongo_docs = connection.collection.find()

    docs = DataFrame(mongo_docs)
    docs.pop('country')
    docs.pop('duration')
    docs.pop('promotion')
    docs.pop('style')
    docs.pop('audience')
    docs.pop('story')
    docs.pop('time')
    docs.pop('key')
    docs.pop('watched')
    
    docs.to_csv('movie_data/docs/data.csv', ",", index=False)

# mongo_export_to_file()