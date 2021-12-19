# -*- coding: utf-8 -*-
# filename  : 3.1_异步加载实例.py
# datatime  : 2021/12/19 下午4:21
# author    : Yannic Zhang
# explain   : None

import requests

# 确定URL
url = 'https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action='

params = {
    'start': 0,
    'limit': 15
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
}

# 发送请求获取响应
response = requests.get(url, headers=headers, params=params)

# 获取数据保存数据
with open('douban.json', 'wb') as f:
    f.write(response.content)
