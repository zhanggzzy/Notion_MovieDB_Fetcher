from pprint import pprint
from src.movie.TMDB import get_movie_detail, get_movie_credits, get_series_season_detail, organize_data, search, get_series_detail, get_series_season_credits
from src.movie.wmdb import organize_wmdb_data, search_with_wmdb, get_wmdb_movie_detail

class Movie:
    
    def __init__(self, title, year=None) -> None:
        self.title = title
        self.tmdb_id = ""
        self.imdb_id = ""
        self.douban_id = ""
        self.original_title = ""
        self.category = ""
        self.director = []
        self.cast = []
        self.genre = []
        self.region = []
        self.year = year
        self.release_date = ""
        self.poster_url = ""
    
    
    def __repr__(self):
        return \
            "title: " + self.title + "\n" + \
            "tmdb_id: " + str(self.tmdb_id) + "\n" + \
            "imdb_id: " + str(self.imdb_id) + "\n" + \
            "douban_id " + self.douban_id + "\n" + \
            "original_title: " + self.original_title + "\n" + \
            "category: " + self.category + "\n" + \
            "director: " + ", ".join(self.director) + "\n" + \
            "cast: " + ", ".join(self.cast) + "\n" + \
            "genre: " + ", ".join(self.genre) + "\n" + \
            "region: " + ", ".join(self.region) + "\n" + \
            "release_date: " + self.release_date + "\n" + \
            "poster_url: " + self.poster_url + "\n"
            

    def generate_data(self, method="TMDB"):
        
        if method == "TMDB":
            # search movie with TMDB
            # results = search_movie_with_TMDB(self.title, primary_release_year=self.year)
            search_results = search(self.title)
            results = []
            
            for r in search_results:
                try:
                    if r['media_type'] == "movie":
                        results.append({
                            'id': r['id'],
                            'title': r['title'],
                            'original_title': r['original_title'],
                            'released_date': r['release_date'],
                            'media_type': '电影'
                        })
                    elif r['media_type'] == "tv":
                        results.append({
                            'id': r['id'],
                            'title': r['name'],
                            'original_title': r['original_name'],
                            'released_date': r['first_air_date'],
                            'media_type': '剧集'
                        })
                except KeyError:
                    continue
                    
            self.select_result(results)
            
            season_detail = None
            if self.category == "电影":
                detail = get_movie_detail(self.tmdb_id)
                credits = get_movie_credits(self.tmdb_id)
            elif self.category == "剧集":
                detail = get_series_detail(self.tmdb_id)
                season_detail = self.select_season(detail)
                credits = get_series_season_credits(self.tmdb_id, season_detail['season_number'])
            
            # pprint(detail.keys())
            # pprint(credits.keys())
            # TODO: organize data
            # pprint(movie_credits)
            # exit()
            organize_data(self, detail, credits, season_detail)
            
        elif method =="wmdb":
            results = search_with_wmdb(self.title)[:10]
            results = [{
                'id': r['doubanId'],
                'title': r['data'][0]['name'],
                'original_title':r['originalName'],
                'released_date':r['dateReleased']
            } for r in results]

            self.douban_id = self.select_result(results)
            movie_detail = get_wmdb_movie_detail(self.douban_id)
            
            organize_wmdb_data(self, movie_detail)
            
    
    def select_result(self, results):
        print("0 - Exit")
        
        for i, r in enumerate(results):
            print("{} - [{}]{} {} ({})".format(i+1, r['media_type'], r['title'], r['original_title'], r['released_date']))
            
        choice = int(input("Enter your choice: "))
        
        if choice == 0:
            exit()
        else:
            self.tmdb_id = results[choice-1]['id']
            self.category = results[choice-1]['media_type']
    
    def select_season(self, detail):
        print("0 - Exit")
        
        for i, r in enumerate(detail['seasons']):
            print("{} - {} ({})".format(i+1, r['name'], r['air_date']))
            
        choice = int(input("Enter your choice: "))
        
        if choice == 0:
            exit()
        else:
            self.title += " " + detail['seasons'][choice-1]['name']
            return get_series_season_detail(self.tmdb_id, detail['seasons'][choice-1]['season_number'])
