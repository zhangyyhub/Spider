# -*- coding: utf-8 -*-
# filename  : 1.10_requests_get.py
# datatime  : 2021/12/18 下午6:13
# author    : Yannic Zhang
# explain   : None

import requests

url = 'https://www.baidu.com/s'
val = input('请输入你要查询的页面: ')

params = {
    'wd': val
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
}

response = requests.get(url, headers=headers, params=params)

data = response.content

with open('{}.html'.format(val), 'wb') as f:
    f.write(data)
