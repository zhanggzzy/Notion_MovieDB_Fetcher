from src.movie.TMDB import search_with_TMDB, get_TMDB_movie_detail, get_TMDB_movie_credits, organize_TMDB_data
from src.movie.wmdb import organize_wmdb_data, search_with_wmdb, get_wmdb_movie_detail

class Movie:
    
    def __init__(self, title) -> None:
        self.title = title
        self.tmdb_id = ""
        self.imdb_id = ""
        self.douban_id = ""
        self.original_title = ""
        self.category = "电影"
        self.director = []
        self.cast = []
        self.genre = []
        self.region = []
        self.release_date = ""
        self.poster_url = ""
    
    
    def __repr__(self):
        return \
            "title: " + self.title + "\n" + \
            "tmdb_id: " + str(self.tmdb_id) + "\n" + \
            "imdb_id: " + self.imdb_id + "\n" + \
            "douban_id " + self.douban_id + "\n" + \
            "original_title: " + self.original_title + "\n" + \
            "category: " + self.category + "\n" + \
            "director: " + ", ".join(self.director) + "\n" + \
            "cast: " + ", ".join(self.cast) + "\n" + \
            "genre: " + ", ".join(self.genre) + "\n" + \
            "region: " + ", ".join(self.region) + "\n" + \
            "release_date: " + self.release_date + "\n" + \
            "poster_url: " + self.poster_url + "\n"
            

    def generate_movie_data(self, method="TMDB"):
        
        if method == "TMDB":
            # search movie with TMDB
            self.tmdb_id = search_with_TMDB(self.title)
            # get movie detail from TMDB
            movie_detail = get_TMDB_movie_detail(self.tmdb_id)
            # get movie credits from TMDB
            movie_credits = get_TMDB_movie_credits(self.tmdb_id)
            
            organize_TMDB_data(self, movie_detail, movie_credits)
            
        elif method =="wmdb":
            self.douban_id = search_with_wmdb(self.title)[0]['doubanId']
            movie_detail = get_wmdb_movie_detail(self.douban_id)
            # print(movie_detail)
            
            organize_wmdb_data(self, movie_detail)
            
        
        # organize movie data
        # movie_item = self.organize_TMDB_data(movie_detail, movie_credits)