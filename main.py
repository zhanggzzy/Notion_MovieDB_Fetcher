import requests
from private import TMDB_apikey, TMDB_api_token, Notion_token, Notion_DB_ID

movie_struct = {
    "parent": {
        "type": "database_id",
        "database_id": Notion_DB_ID
    },
    "properties": {
        "中文片名": {
            "title": [
                {
                    "type": "text",
                    "text": {
                        "content": "默认中文片名"
                    }
                }
            ]
        },
        "片名": {
            "rich_text": [
                {
                    "type": "text",
                    "text": {
                        "content": "默认片名",  
                    }
                }
            ]
        },
        "分类": {
            "select": {
                "name": "电影",
            }
        },
        "导演": {
            "Multi-Select": [
                {
                    "name": "Steven Spielberg"
                }
            ]
        },
        "主演": {
            "Multi-Select": [
                {
                    "name": "Leonardo DiCaprio"
                },
                {
                    "name": "Tom Hanks"
                },
                # {
                #     ""
                # }
            ]
        }
    }
}


def get_request(site, url):
    if site == "TMDB":
        header = {
            'Content-Type': 'application/json; charset=utf-8',
            'Authorization': 'Bearer ' + TMDB_api_token
        }
    elif site == "Notion":
        header = {
            'Authorization': 'Bearer ' + Notion_token,
            'Notion-Version': '2022-06-28'
        }
    
    return requests.get(url, headers=header).json()


def is_chinese(uchar):
    if uchar >= u'\u4e00' and uchar <= u'\u9fa5':
        return True
    else:
        return False
 

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

    def search_with_TMDB(self, query, language="zh-CN", page=1, include_adult=False, 
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



    def get_TMDB_movie_detail(self, TMDB_id, language="zh-CN"):
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


    def get_TMDB_movie_credits(self, TMDB_id, language="zh-CN"):
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


    def get_alt_title(self, TMDB_id):
        
        # build url
        url = "https://api.themoviedb.org/3/movie/"
        url += str(TMDB_id)
        url += "/alternative_titles?"
        url += "country=CN"
        
        return get_request("TMDB", url)


    def organize_TMDB_data(self, movie_detail, movie_credits):
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
        
        return movie_item
    
    def generate_movie_data(self):
        # search movie with TMDB
        movie_id = self.search_with_TMDB(self.title)
        # get movie detail from TMDB
        movie_detail = self.get_TMDB_movie_detail(movie_id)           
        # get movie credits from TMDB
        movie_credits = self.get_TMDB_movie_credits(movie_id)
        
        print(movie_credits)
    
        # organize movie data
        # movie_item = self.organize_TMDB_data(movie_detail, movie_credits)
    

class Notion:
    def get_notion_info(Notion_DB_ID):
        url = "https://api.notion.com/v1/databases/" + Notion_DB_ID
        return get_request("Notion", url)


    def insert_into_notion(Notion_token, Notion_DB_ID, data):
        header = {
            'Authorization': 'Bearer ' + Notion_token,
            'Notion-Version': '2022-06-28'
        }
        url = "https://api.notion.com/v1/pages"
        response = requests.post(url, headers=header, json=data)
        return response

if __name__ == '__main__':
    # movie_name = input("Enter movie name: ")
    movie_name = "让子弹飞"
    
    movie = Movie(movie_name)
    
    movie_item = movie.generate_movie_data()

    # print(movie_item)

    # print(get_notion_info(Notion_token, Notion_DB_ID))
    # print(insert_into_notion(Notion_token, Notion_DB_ID, data))