# -*- coding: utf-8 -*-
# filename  : 1.9_requests_commonMethod.py
# datatime  : 2021/12/18 下午6:01
# author    : Yannic Zhang
# explain   : None

from urllib.parse import urlencode
import requests

jurl = 'https://movie.douban.com/j/search_subjects'
ua = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"

d = {
    'type': 'movie',
    'tag': '热门',
    'page_limit': 20,
    'page_start': 0
}

url = '{}?{}'.format(jurl, urlencode(d))
print(url)

response = requests.request('GET', url, headers={'User-agent': ua})

with response:
    print(1, response.text)               # text
    print(2, response.content)            # bytes
    print(2, response.status_code)        # status
    print(3, response.url)                # url
    print(4, response.headers)            # 响应头
    print(5, response.request.headers)    # 响应对应的请求头
    print(6, response.cookies)            # 响应的cookie（经过了set-cookie动作）
    print(7, response.request._cookies)   # 响应对应请求的cookie