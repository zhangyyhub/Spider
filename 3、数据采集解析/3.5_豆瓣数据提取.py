# -*- coding: utf-8 -*-
# filename  : 3.5_豆瓣数据提取.py
# datatime  : 2021/12/19 下午4:59
# author    : Yannic Zhang
# explain   : None

import json
import jsonpath
import requests

url = 'https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start=0&limit=20'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'
}

response = requests.get(url, headers=headers)

str_data = response.text
python_data = json.loads(str_data)

movie_data = jsonpath.jsonpath(python_data, '$..title')
print(movie_data)

score_data = jsonpath.jsonpath(python_data, '$..score')
print(score_data)

# 电影数据整合方法1
movie_dict = {}
for i in range(len(movie_data)):
    # {'电影名':评分}
    movie_dict[movie_data[i]] = score_data[i]
print(movie_dict)

# 电影数据整合方法2
movie_dict = dict(zip(movie_data, score_data))
print(movie_dict)

# 转换为json数据并存入json文件
with open('movie.json', 'w', encoding='utf-8')as f:
    json.dump(movie_dict, f, ensure_ascii=False)
