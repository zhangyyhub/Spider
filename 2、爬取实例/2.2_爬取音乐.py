# -*- coding: utf-8 -*-
# filename  : 2.2_爬取音乐.py
# datatime  : 2021/12/18 下午8:16
# author    : Yannic Zhang
# explain   : None

import requests

url = 'https://m801.music.126.net/20211218203836/f72cf56decaf26711b6859dc3f9d6fcc/jdyyaac/obj/w5rDlsOJwrLDjj7CmsOj/9879675715/aa46/c29c/bef7/cb34148aa2b1cb9fcf6b633ed7822b19.m4a'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
}

response = requests.get(url, headers=headers)

data = response.content

with open('变废为宝.mp3', 'wb') as f:
    f.write(data)
