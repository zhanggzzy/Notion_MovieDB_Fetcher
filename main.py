from src.movie.model import Movie

if __name__ == '__main__':
    # movie_name = input("Enter movie name: ")
    movie_name = "让子弹飞"
    
    movie = Movie(movie_name)
    
    print(movie)
    
    # movie_item = movie.generate_movie_data()

    # print(movie_item)

    # print(get_notion_info(Notion_token, Notion_DB_ID))
    # print(insert_into_notion(Notion_token, Notion_DB_ID, data))
