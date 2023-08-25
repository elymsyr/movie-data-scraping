from pymongo import MongoClient

class MongoConnectionFinder():
    cluster = MongoClient("mongodb+srv://admin:vDFk9UU5UhJ8FA10@movie-rec-data.l2nnka0.mongodb.net/")
    db = cluster["main_movie_data"]
    collection = db["movie-urls"]

    def insert(self, data):
        self.collection.insert_one({'url': data, 'crawled': 0})

    def find_all(self):
        movies = []
        results = self.collection.find()
        for result in results:
            movies.append(f"https://tarzifilm.com{result['url']}")
        if len(movies) == 0:
            return ["https://tarzifilm.com/"]
        else:
            return movies
        
    def find_to_crawl(self):
        movies = []
        results = self.collection.find({'crawled': 0})
        for result in results:
            movies.append(f"https://tarzifilm.com{result['url']}")
        return movies

    def check_exists(self, data):
        results = self.collection.find_one({'url': data})
        if results != None:
            return 0
        else:
            return 1

    def clearDb(self):
        self.collection.delete_many({'url':'https://tarzifilm.comNone'})
        self.collection.delete_many({'url':'None'})
    def clearDb_all(self):
        self.collection.delete_many({})    

    def update_state(self, url):
        self.collection.update_one({'url': url}, {"$set":{'crawled': 1}})
    
    def update_state_reset(self):
        self.collection.update_many({}, {"$set":{'crawled': 0}})
        
# con = MongoConnectionFinder()
# con.clearDb()