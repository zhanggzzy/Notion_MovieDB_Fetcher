class Movie:
    
    def __init__(self, title) -> None:
        self.title = title
        self.original_title = ""
        self.category = ""
        self.director = []
        self.cast = []
        self.genre = []
        self.region = []
        self.release_date = ""
        self.poster_url = ""
    
    
    def __repr__(self):
        repr = "<Movie: " + self.title + ">"
        return repr

    
    def generate_movie_data(self):
        # search movie with TMDB
        movie_id = self.search_with_TMDB(self.title)
        # get movie detail from TMDB
        movie_detail = self.get_TMDB_movie_detail(movie_id)           
        # get movie credits from TMDB
        movie_credits = self.get_TMDB_movie_credits(movie_id)
        
        # print(movie_credits)
    
        # organize movie data
        # movie_item = self.organize_TMDB_data(movie_detail, movie_credits)