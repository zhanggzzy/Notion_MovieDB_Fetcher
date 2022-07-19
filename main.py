import requests
import json
from private import TMDB_apikey

def search_with_TMDB(api_key=TMDB_apikey, language="zh-CN", query="", page=1, 
                        include_adult=False, region="", year="", primary_release_year=""):
    url = "https://api.themoviedb.org/3/search/movie?"
    url += "api_key=" + api_key
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
    
    r = requests.get(url)
    return r.json()


if __name__ == '__main__':
    print('Movie Fetcher')
    result = search_with_TMDB(query="蝙蝠侠")
    print(json.dumps(result, indent=4))