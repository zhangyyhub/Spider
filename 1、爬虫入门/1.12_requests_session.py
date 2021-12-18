# -*- coding: utf-8 -*-
# filename  : 1.12_requests_session.py
# datatime  : 2021/12/18 下午6:28
# author    : Yannic Zhang
# explain   : None

import requests

ua = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'

urls = ['https://www.baidu.com/s?&wd=%E8%83%8C%E6%99%AF', 'https://www.baidu.com/s?&wd=%E8%83%8C%E6%99%AF']

session = requests.Session()
with session:
    for url in urls:
        response = session.get(url, headers={'User-Agent': ua})

        with response:
            print(type(response))
            print(response.url)
            print(response.status_code)
            print(response.request.headers)  # 请求头
            print(response.cookies)          # 响应的cookie
            print(response.text[:20])        # HTML内容
