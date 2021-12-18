# -*- coding: utf-8 -*-
# filename  : 1.8_urllib3库.py
# datatime  : 2021/12/18 下午5:49
# author    : Yannic Zhang
# explain   : None

from urllib.parse import urlencode
import urllib3

url = 'https://movie.douban.com/j/search_subjects'
ua = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'

d = {
    'type': 'movie',
    'tag': '热门',
    'page_limit': 20,
    'page_start': 0
}

with urllib3.PoolManager() as http:
    responce = http.request('GET', '{}?{}'.format(url, urlencode(d)), headers={'User-agent': ua})
    print(type(responce))    # <class 'urllib3.response.HTTPResponse'>
    print(responce.status, responce.reason)
    print(responce.data)
    print(responce.headers)
