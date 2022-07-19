# Notion电影数据获取 Notion_MovieDB_Fetcher 

自用的电影数据获取脚本，从开放影视API获取电影数据，对应插入到Notion中电影数据库的对应参数中。

A self-use script to fetch data from public APIs, corresponding to the parameters of the movie database in Notion.

## Notion 数据库结构 Notion Database Structure

| 字段名称 | 字段类型 | 字段描述 |
| -------- | ------- | ------- |
| 片名 | Title | 该片中文片名 |
| 外语片名 | Text | 英语片名或发行地区语言片名 |
| 分类 | Select | 该片所属类型，电影、纪录片、或剧集 |
| 导演 | Multi-select | 该片导演 |
| 主演 | Multi-select | 该片主演，记录5人，如果有知名演员则记录更多 |
| 类型 | Multi-select | 该片涉及的类型 |
| 国家/地区 | Multi-select | 该片发行的国家或地区 |
| 上映年份 | Select | 该片上映的年份 |
| 豆瓣 | URL | 该片的豆瓣页面 |
| 海报 | File&Media | 该片的海报 |

## 获取数据方式 Get Data Method

输入电影中文名称，获取电影数据。

Enter the Chinese name of the movie, and get the movie data.

## API

- [The Movie DB](https://www.themoviedb.org/documentation/api)
- [IMDB](https://developer.imdb.com/)
