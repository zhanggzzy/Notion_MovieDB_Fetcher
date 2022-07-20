import requests
import json
from private import TMDB_apikey, TMDB_api_token, Notion_token, Notion_DB_ID

def search_with_TMDB(query, api_key=TMDB_apikey, language="zh-CN", page=1, 
                        include_adult=False, region=None, year=None, primary_release_year=None):
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
        int: movie ID in TMDB
    """

    header = {
        'Content-Type': 'application/json; charset=utf-8',
        'Authorization': 'Bearer ' + TMDB_api_token
        }

    url = "https://api.themoviedb.org/4/search/movie?"
    # url += "api_key=" + api_key
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
    
    movie_id = requests.get(url, headers=header).json()["results"][0]["id"]

    if movie_id:
        return movie_id
    else:
        raise Exception("No movie found")



def get_TMDB_movie_detail(TMDB_id, api_key=TMDB_apikey, language="zh-CN"):
    header = {
        'Content-Type': 'application/json; charset=utf-8',
        'Authorization': 'Bearer ' + TMDB_api_token
        }

    url = "https://api.themoviedb.org/4/movie/"
    url += str(TMDB_id)
    # url += "?api_key=" + TMDB_apikey
    url += "&language=" + language
    movie_data = requests.get(url, header=header).json()
    return movie_data


def get_TMDB_movie_credits(TMDB_id, api_key=TMDB_apikey, language="zh-CN"):

    header = {
        'Content-Type': 'application/json; charset=utf-8',
        'Authorization': 'Bearer ' + TMDB_api_token
        }

    url = "https://api.themoviedb.org/4/movie/"
    url += str(TMDB_id)
    url += "/credits"
    # url += "?api_key=" + TMDB_apikey
    url += "&language=" + language
    movie_credits = requests.get(url, header=header).json()
    return movie_credits


def get_TMDB_movie_poster(img_url):
    url = "https://image.tmdb.org/t/p/w1280" + img_url
    return url


def organize_TMDB_data(TMDB_id):
    movie_data = get_TMDB_movie_detail(TMDB_id)
    movie_credits = get_TMDB_movie_credits(TMDB_id)

    
    
    return movie_data, movie_credits


if __name__ == '__main__':
    # print('Movie Fetcher')
    result = search_with_TMDB(query="蝙蝠侠")
    print(result)
    # print(TMDB_apikey)
    # print(TMDB_api_token)