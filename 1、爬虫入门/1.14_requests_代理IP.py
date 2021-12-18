# -*- coding: utf-8 -*-
# filename  : 1.14_requests_代理IP.py
# datatime  : 2021/12/18 下午6:54
# author    : Yannic Zhang
# explain   : None

import requests

url = 'http://httpbin.org/get'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
}

proxies = {
    'http': 'http://114.99.8.14:4231'
}

response = requests.get(url, headers=headers, proxies=proxies, timeout=3)

print(response.text)    # 代理IP不可用直接报错
