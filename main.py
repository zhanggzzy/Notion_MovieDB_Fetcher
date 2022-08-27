from re import search
from src.notion.notion import Notion
from src.movie.model import Movie
from data.private import Notion_token, Notion_DB_ID
from pprint import pp, pprint

if __name__ == '__main__':
    
    
    movie_name = input("Enter movie name: ")
    search_method = "TMDB"
    movie = Movie(movie_name)
    
    movie.generate_data(method=search_method)

    pprint(movie)
    # exit()
    
    notion = Notion(Notion_token, Notion_DB_ID)
    notion.insert_into_notion(movie)
