import requests
from helper import get_request

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