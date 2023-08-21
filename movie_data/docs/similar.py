from random import randint
from mongo_crawl import get_one, comp
from collections import Counter
from math import ceil
def similarity(list_one, list_two):
    a_vals = Counter(list_one)
    b_vals = Counter(list_two)
    words  = list(a_vals.keys() | b_vals.keys())
    a_vect = [a_vals.get(word, 0) for word in words]
    b_vect = [b_vals.get(word, 0) for word in words]
    len_a  = sum(av*av for av in a_vect) ** 0.5
    len_b  = sum(bv*bv for bv in b_vect) ** 0.5
    dot    = sum(av*bv for av,bv in zip(a_vect, b_vect)) 
    try:
        cosine = dot / (len_a * len_b)
    except:
        cosine = 0.05
    return cosine
def similar_finder(number_of_search, movie=None):
    if movie == None:
        random_movie = randint(0,2000)
        movie = get_one(random_movie)
        while movie['name'] == '':
            random_movie = randint(0,2000)
            movie = get_one(random_movie)
    print("\n")
    print(movie['name'], movie['genre'], movie['url'])
    print("SIMILARS:")
    similar_movies = comp(movie)
    for mov in similar_movies:
        rank_a = similarity(movie['style'], mov['style'])*10
        rank_b = similarity(movie['story'], mov['story'])*10
        rank_c = similarity(movie['genre'], mov['genre'])*10
        mov['audience'] = rank_a*rank_b*rank_c
    print(f"{len(similar_movies)} movie found.")
    sorterd_founded = sorted(similar_movies, key=lambda d: d['audience'])
    sorterd_founded.reverse()
    for mov in sorterd_founded[:number_of_search+1]:
        if mov['url'] != movie['url']:
            print(f"{ceil(mov['audience'])} - {mov['name']} --> {mov['url']}")

for _ in range(3):
    similar_finder(10)