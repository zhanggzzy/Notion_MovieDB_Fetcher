from data.private import TMDB_api_token, Notion_token, Notion_token
import requests

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
    elif site == "wmdb":
        header = {}
    
    return requests.get(url, headers=header).json()


def post_request(site, url, data):
    if site == "Notion":
        header = {
            'Authorization': 'Bearer ' + Notion_token,
            'Notion-Version': '2022-06-28'
        }
    
    return requests.post(url, headers=header, json=data).json()


def is_chinese(uchar):
    if uchar >= u'\u4e00' and uchar <= u'\u9fa5':
        return True
    else:
        return False
