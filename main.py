from src.notion.notion import Notion
from src.movie.model import Movie
from data.private import Notion_token, Notion_DB_ID
from pprint import pprint

if __name__ == '__main__':
    movie_name = input("Enter movie name: ")
    search_method = input("Enter search method, either 'TMDB' or 'wmdb': ")
    movie = Movie(movie_name)
    
    movie.generate_movie_data(method=search_method)

    notion = Notion(Notion_token, Notion_DB_ID)
    
    notion.insert_into_notion(movie)
