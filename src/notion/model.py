from data.private import Notion_DB_ID

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
            "multi_select": []
        },
        "主演": {
            "multi_select": []
        },
        "类型": {
            "multi_select": []
        },
        "国家/地区": {
            "multi_select": []
        },
        "上映年份": {
            "select": {
                "name": "2020",
            }
        },
        "豆瓣": {
            "url": ""
        },
        "海报": {
            "type": "files",
            "files": []
        }
    }
}