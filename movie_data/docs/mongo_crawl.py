from pymongo import MongoClient


cluster = MongoClient("mongodb+srv://admin:vDFk9UU5UhJ8FA10@movie-rec-data.l2nnka0.mongodb.net/")
db = cluster["main_movie_data"]
collection = db["movie-data"]

SELECTORS = ['url', 'name', 'genre', 'duration', 'summary', 'finders', 'audience', 'movie', 'time', 'key', 'watched']

def insert(data):
    insert_data = {
        'url': data[0],
        'name': data[1],
        'genre': data[2],
        'country': data[3],
        'duration': data[4],
        'promotion': data[5],
        'style': data[6],
        'audience': data[7],
        'story': data[8],
        'time': data[9],
        'key': data[10],
        'watched': data[11],
        }
    collection.insert_one(insert_data)
    
def find_all():
    movies = []
    results = collection.find()
    for result in results:
        movies.append(result['url'])
    return movies
    
def comp(movie):
    similar_movies = []
    results = collection.find({'$and':[{"genre":{"$in":movie['genre']}},{"style":{"$in":movie['style']}},{"story":{"$in":movie['story']}},{"audience":{"$in":movie['audience']}}]})
    for mov in results:
        similar_movies.append(mov)
    if similar_movies == []:
        results = collection.find({'$and':[{"genre":{"$in":movie['genre']}},{"story":{"$in":movie['story']}}, {"style":{"$in":movie['style']}}]})
        similar_movies = []
        for mov in results:
            similar_movies.append(mov)
    if similar_movies == []:
        results = collection.find({'$and':[{"genre":{"$in":movie['genre']}}, {"style":{"$in":movie['style']}}]})
        similar_movies = []
        for mov in results:
            similar_movies.append(mov)
    if similar_movies == []:
        results = collection.find({"genre":{"$in":movie['genre']}})
        similar_movies = []
        for mov in results:
            similar_movies.append(mov)
    return similar_movies

def get_one(index):
    results = collection.find().limit(1).skip(index).next()
    return results

def clearDb():
    # collection.delete_many({})
    collection.delete_many({'url':'None'})

def updateWatched(state, url):
    collection.update_one({'url':f'{url}'}, {"$set":{'watched': state}})
