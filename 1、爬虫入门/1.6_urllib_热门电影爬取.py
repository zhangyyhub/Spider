# -*- coding: utf-8 -*-
# filename  : 1.6_urllib_热门电影爬取.py
# datatime  : 2021/12/18 下午5:15
# author    : Yannic Zhang
# explain   : None

from urllib.parse import urlencode
from urllib.request import Request, urlopen
import json
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

ua = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
url = 'https://movie.douban.com/j/search_subjects'

d = {
    'type': 'movie',
    'tag': '热门',
    'page_limit': 20,
    'page_start': 0
}

req = Request('{}?{}'.format(url, urlencode(d)), headers={'User-agent': ua})

try:
    with urlopen(req) as res:
        data = res.read().decode('utf-8')
        # print(type(data), data)
        dictdata = json.loads(data)
        # print(type(dictdata), dictdata)

        for movie in dictdata.get('subjects'):
            # print(type(movie), movie)
            print('movie={} url={}'.format(movie.get('title'), movie.get('url')))

except Exception as errmsg:
    print('error message: '.format(errmsg))
