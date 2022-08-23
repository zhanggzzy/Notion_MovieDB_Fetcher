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