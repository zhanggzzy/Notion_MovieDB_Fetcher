from helper import get_request

def search_with_TMDB(movie, query, language="zh-CN", page=1, include_adult=False, 
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
        int: movie ID in TMDB
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
    
    movie_id = get_request("TMDB", url)["results"][0]["id"]

    if movie_id:
        return int(movie_id)
    else:
        raise Exception("No movie found")



def get_TMDB_movie_detail(movie, TMDB_id, language="zh-CN"):
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


def get_TMDB_movie_credits(movie, TMDB_id, language="zh-CN"):
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


def get_TMDB_movie_poster(img_url):
    url = "https://image.tmdb.org/t/p/w1280" + img_url
    return url


def get_alt_title(movie, TMDB_id):
    
    # build url
    url = "https://api.themoviedb.org/3/movie/"
    url += str(TMDB_id)
    url += "/alternative_titles?"
    url += "country=CN"
    
    return get_request("TMDB", url)


def organize_TMDB_data(movie, movie_detail, movie_credits):
    pass
    
    # set original title
    # movie_item['properties']['片名']['rich_text'][0]['text']['content'] = movie_data['original_title']

    # print(movie_data['title'])    
    # set director
    # print("movie_credits: ")
    # cast = movie_credits['cast']
    # print(cast)
    # for i in range(len(cast)):
    #     print(cast[i]['known_for_department'])
    
    
    # print(movie_data)
    # print(movie_credits)
    
    # return movie_item