from csv import reader

def search_by_name(key):
    with open('movie_data/docs/data.csv', 'r', encoding='utf-8') as f:
        read = reader(f)
        lines = [ row for row in read if key.strip().lower() in row[2].strip().lower() ]
        for item in lines:
            print(item[0])
def search_by_cat(key):
    with open('movie_data/docs/data.csv', 'r', encoding='utf-8') as f:
        read = reader(f)
        lines = [ row for row in read if key.strip().lower() in row[3].strip().lower() ]
        for item in lines:
            print(item[0])
# search_by_cat('aksiyon')
# search_by_name('avengers')