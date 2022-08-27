from webbrowser import get
from src.helper import get_request
from pprint import pprint


def search_movie(query, language="zh-CN", page=1, include_adult=False, 
                    region=None, year=None, primary_release_year=None):
    """Search movie  with The Movie Database

    Args:
        query (str): content to search
        api_key (str, optional): API key applied from the platform. Defaults to TMDB_apikey.
        language (str, optional): search result language. Defaults to "zh-CN".
        page (int, optional): page number of result. Defaults to 1.
        include_adult (bool, optional): whether adult content included. Defaults to False.
        region (str, optional): region of the movie, used to restrict the result. Defaults to None.
        year (int, optional): Defaults to None.
        primary_release_year (int, optional): Defaults to None.

    Raises:
        Exception: No result found for the query.

    Returns:
        search result
    """
    
    # build url
    url = "https://api.themoviedb.org/3/search/movie?"
    url += "&language=" + language
    url += "&query=" + query
    url += "&page=" + str(page)
    url += "&include_adult=" + str(include_adult)

    if region:
        url += "&region=" + region
    if year:
        url += "&year=" + year
    if primary_release_year:
        url += "&primary_release_year=" + primary_release_year
    
    return get_request("TMDB", url)['results']


def search(query, language="zh-CN", page=1, include_adult=False, region=None):
    
    url = "https://api.themoviedb.org/3/search/multi?"
    url += "&language=" + language
    url += "&query=" + query
    url += "&page=" + str(page)
    url += "&include_adult=" + str(include_adult)
    if region:
        url += "&region=" + region
        
    return get_request("TMDB", url)['results']
   


def get_movie_detail(TMDB_id, language="zh-CN"):
    """fetches movie detail from TMDB

    Args:
        TMDB_id (int): movie id in TMDB
        language (str, optional): movie result language. Defaults to "zh-CN".

    Returns:
        dict: a dict of movie detail
    """
    
    # build url
    url = "https://api.themoviedb.org/3/movie/"
    url += str(TMDB_id) + "?"
    url += "language=" + language
    
    return get_request("TMDB", url)


def get_movie_credits(TMDB_id, language="zh-CN"):
    """fetches movie credits from TMDB

    Args:
        TMDB_id (int): movie id in TMDB
        language (str, optional): result language. Defaults to "zh-CN".

    Returns:
        dict: a dict of movie credits
    """
    
    # build url
    url = "https://api.themoviedb.org/3/movie/"
    url += str(TMDB_id)
    url += "/credits?"
    url += "language=" + language
    
    return get_request("TMDB", url)


def get_movie_poster(TMDB_id, language):
    url = "https://api.themoviedb.org/3/movie/"
    url += str(TMDB_id) + "/images?"
    url + "language=" + language
    
    poster_url_pro = "https://www.themoviedb.org/t/p/w1280"
    
    poster = get_request("TMDB", url)
    poster = [x for x in poster['posters'] if x['iso_639_1'] == language]
    
    # select the first one
    try:
        poster_url = poster_url_pro + poster[0]['file_path']
    except IndexError:
        poster_url = None
    return poster_url

def get_series_season_poster(TMDB_id, season_number, language="zh-CN"):
    url = "https://api.themoviedb.org/3/tv/{tv_id}/season/{season_number}/images".format(tv_id=TMDB_id, season_number=season_number)
    url += "?language=" + language
    poster_url_pro = "https://www.themoviedb.org/t/p/w1280"
    poster = get_request("TMDB", url)
    poster = [x for x in poster['posters'] if x['iso_639_1'] == language]
    # select the first one
    try:
        poster_url = poster_url_pro + poster[0]['file_path']
    except IndexError:
        poster_url = None
    return poster_url

def get_series_detail(TMDB_id, language="zh-CN"):
    url = "https://api.themoviedb.org/3/tv/{tv_id}?".format(tv_id=TMDB_id)
    url += "language=" + language
    return get_request("TMDB", url)


def get_series_season_detail(TMDB_id, season_number, language="zh-CN"):
    url = "https://api.themoviedb.org/3/tv/{tv_id}/season/{season_number}".format(tv_id=TMDB_id, season_number=season_number)
    url += "?language=" + language
    return get_request("TMDB", url)

def get_series_season_credits(TMDB_id, season_number, language="zh-CN"):
    url = "https://api.themoviedb.org/3/tv/{tv_id}/season/{season_number}/credits".format(tv_id=TMDB_id, season_number=season_number)
    url += "?language=" + language
    return get_request("TMDB", url)


def organize_data(movie, detail, credits, season_detail=None):
    # pprint(season_detail)
    
    if movie.category == "电影":
        movie.title = detail['title']
        movie.original_title = detail['original_title']
        movie.imdb_id = detail['imdb_id']
        movie.genre = [detail["genres"][x]["name"] for x in range(len(detail["genres"]))]
        movie.poster_url = get_movie_poster(movie.tmdb_id, detail["original_language"]) 
        movie.release_date = detail['release_date']
        movie.region = [detail['production_countries'][x]['name'] for x in range(len(detail['production_countries']))]
        num_of_cast = min(len(credits['cast']), 10)
        movie.cast = [credits['cast'][x]['name'] for x in range(num_of_cast)]
        movie.director = [credits['crew'][x]['name'] for x in range(len(credits['crew'])) if credits['crew'][x]['job'] == "Director"]
    elif movie.category == "剧集":
        movie.title = detail['name'] + " " + season_detail['name']
        movie.original_title = detail['original_name']
        movie.genre = [detail["genres"][x]["name"] for x in range(len(detail["genres"]))]
        movie.poster_url = get_series_season_poster(movie.tmdb_id, season_detail['season_number'], detail["original_language"])
        if movie.poster_url is None:
            movie.poster_url = "https://www.themoviedb.org/t/p/w1280" + detail['poster_path']
        movie.release_date = season_detail['air_date']
        movie.region = [detail['production_countries'][x]['name'] for x in range(len(detail['production_countries']))]
        num_of_cast = min(len(credits['cast']), 10)
        movie.cast = [credits['cast'][x]['name'] for x in range(num_of_cast)]
        movie.director = [detail['created_by'][x]['name'] for x in range(len(detail['created_by']))]
