from src.notion.notion import Notion
from src.movie.model import Movie
from data.private import Notion_token, Notion_DB_ID
from pprint import pprint

if __name__ == '__main__':
    # movie_name = input("Enter movie name: ")
    movie_name = "幽灵公主"
    movie = Movie(movie_name)
    movie.generate_movie_data(method="wmdb")
    
    # print(movie)

    notion = Notion(Notion_token, Notion_DB_ID)
    
    notion.insert_into_notion(movie)
