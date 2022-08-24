from pprint import pprint
from src.helper import get_request, post_request
from .model import movie_struct

class Notion:
    
    def __init__(self, Notion_token, Notion_DB_ID) -> None:
        self.Notion_token = Notion_token
        self.Notion_DB_ID = Notion_DB_ID
        self.data = movie_struct.copy()
    
    def get_notion_info(self):
        # url = "https://api.notion.com/v1/databases/" + self.Notion_DB_ID
        url = "https://api.notion.com/v1/pages/f2421c77afde429d9341c016b4613fda"

        return get_request("Notion", url)


    def insert_into_notion(self, movie):
        
        self.modify_title("中文片名", movie.title)
        self.modify_rich_text("片名", movie.original_title)
        # self.modify_select("分类", movie.category)
        self.modify_multi_select("导演", movie.director)
        self.modify_multi_select("主演", movie.cast)
        self.modify_multi_select("类型", movie.genre)
        self.modify_multi_select("国家/地区", movie.region)
        self.modify_select("上映年份", movie.release_date.split('-')[0])
        douban_url = "https://www.douban.com/subject/" + movie.douban_id
        self.modify_url("豆瓣", douban_url)
        self.modify_files("海报", movie.poster_url)
        
        pprint(self.data)
        # print(self.data)
        
        
        url = "https://api.notion.com/v1/pages"
        return 0
        # return post_request("Notion", url, self.data)
    
    def modify_title(self, key, value):
        self.data['properties'][key]['title'] = [{
            'type': 'text', 
            'text': {
                'content': value
                }
            }]
        
        
    def modify_rich_text(self, key, value):
        self.data['properties'][key]['rich_text'] = [{
            'type': 'text',
            'text': {
                'content': value
                }
            }]
        
        
    def modify_select(self, key, value):
        self.data['properties'][key]['select']['name'] = value
    
    def modify_multi_select(self, key, value):
        self.data['properties'][key]['multi_select'] = [{'name': v} for v in value]
    
    def modify_url(self, key, value):
        self.data['properties'][key]['url'] = value
    
    def modify_files(self, key, value):
        self.data['properties'][key]['files'] = [{
            "type": "external",
            "name": "poster",
            "external": {
                "url": value
            }
        }]
    