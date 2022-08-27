# https://github.com/iiiiiii1/douban-imdb-api

from src.helper import get_request

def search_with_wmdb(query, limit=10, skip=0, lang='Cn', year=None):
    url = "https://api.wmdb.tv/api/v1/movie/search?q=" + query + "&limit=" + str(limit) + "&skip=" + str(skip) + "&lang=" + lang
    if year:
        url += "&year=" + year
    return get_request("wmdb", url)


def get_wmdb_movie_detail(douban_id):
    url = "https://api.wmdb.tv/movie/api?"
    url += "id=" + douban_id
    
    return get_request("wmdb", url)

def organize_wmdb_data(movie, movie_detail):
    movie.title = movie_detail['data'][0]['name']
    movie.original_title = movie_detail['originalName']
    movie.director = [movie_detail['director'][x]['data'][0]['name'] for x in range(len(movie_detail['director']))]
    movie.cast = [movie_detail['actor'][x]['data'][0]['name'] for x in range(len(movie_detail['actor']))][:5]
    movie.genre = movie_detail['data'][0]['genre'].split('/')
    movie.region = movie_detail['data'][0]['country'].split(',')
    movie.release_date = movie_detail['dateReleased']
    movie.poster_url = movie_detail['data'][0]['poster']
