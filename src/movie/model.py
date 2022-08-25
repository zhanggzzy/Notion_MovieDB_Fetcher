from pprint import pprint
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
            results = search_with_TMDB(self.title)
            results = [{
                'id': r['id'], 
                'title': r['title'], 
                'original_title':r['original_title'], 
                'released_date': r['release_date']
            } for r in results]
            
            self.tmdb_id = self.select_movie(results)
            # get movie detail from TMDB
            movie_detail = get_TMDB_movie_detail(self.tmdb_id)
            # get movie credits from TMDB
            movie_credits = get_TMDB_movie_credits(self.tmdb_id)
            
            organize_TMDB_data(self, movie_detail, movie_credits)
            
        elif method =="wmdb":
            results = search_with_wmdb(self.title)[:10]
            results = [{
                'id': r['doubanId'],
                'title': r['data'][0]['name'],
                'original_title':r['originalName'],
                'released_date':r['dateReleased']
            } for r in results]

            self.douban_id = self.select_movie(results)
            movie_detail = get_wmdb_movie_detail(self.douban_id)
            
            organize_wmdb_data(self, movie_detail)
            
    
    def select_movie(self, results):
        print("0 - Exit")
        for i, r in enumerate(results):
            print("{} - {}\n\t{}\n\t{}".format(i+1, r['title'], r['original_title'], r['released_date']))
        choice = int(input("Enter your choice: "))
        
        if choice == 0:
            exit()
        
        return results[choice-1]['id']
    