from src.helper import get_request

def search_with_TMDB(query, language="zh-CN", page=1, include_adult=False, 
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



def get_TMDB_movie_detail(TMDB_id, language="zh-CN"):
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


def get_TMDB_movie_credits(TMDB_id, language="zh-CN"):
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


def get_TMDB_movie_poster(TMDB_id, language):
    url = "https://api.themoviedb.org/3/movie/"
    url += str(TMDB_id) + "/images?"
    url + "language=" + language
    
    poster_url_pro = "https://www.themoviedb.org/t/p/w1280"
    
    poster = get_request("TMDB", url)
    poster = [x for x in poster['posters'] if x['iso_639_1'] == language]
    
    # select the first one
    poster_url = poster_url_pro + poster[0]['file_path']
    
    return poster_url

def organize_TMDB_data(movie, movie_detail, movie_credits):
    
    movie.original_title = movie_detail["original_title"]
    movie.imdb_id = movie_detail["imdb_id"]
    movie.genre = [movie_detail["genres"][x]["name"] for x in range(len(movie_detail["genres"]))]

    movie.poster_url = get_TMDB_movie_poster(movie.tmdb_id, movie_detail["original_language"])    
    
    movie.release_date = movie_detail["release_date"]
    movie.region = [movie_detail['production_countries'][x]['name'] for x in range(len(movie_detail['production_countries']))]
    
    # FIXME: list out of range
        # Traceback (most recent call last):
        # File "d:/Workspace/Notion_MovieDB_Fetcher/main.py", line 11, in <module>
        # movie.generate_movie_data(method=search_method)
        # File "d:\Workspace\Notion_MovieDB_Fetcher\src\movie\model.py", line 48, in generate_movie_data
        # organize_TMDB_data(self, movie_detail, movie_credits)
        # File "d:\Workspace\Notion_MovieDB_Fetcher\src\movie\TMDB.py", line 112, in organize_TMDB_data
        # movie.cast = [movie_credits['cast'][x]['name'] for x in range(5)]
        # File "d:\Workspace\Notion_MovieDB_Fetcher\src\movie\TMDB.py", line 112, in <listcomp>
        # movie.cast = [movie_credits['cast'][x]['name'] for x in range(5)]
        # IndexError: list index out of range
    movie.cast = [movie_credits['cast'][x]['name'] for x in range(5)]
    
    movie.director = [movie_credits['crew'][x]['name'] for x in range(len(movie_credits['crew'])) if movie_credits['crew'][x]['job'] == "Director"]
