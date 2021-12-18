# -*- coding: utf-8 -*-
# filename  : 2.3_爬取视频.py
# datatime  : 2021/12/18 下午8:25
# author    : Yannic Zhang
# explain   : None

import requests

url = 'https://vodkgeyttp8.vod.126.net/cloudmusic/e0c3/core/c425/a0ebb346a2820d30b614068c0faba244.mp4?wsSecret=c506363c4d9b9eaaf82d7df551584218&wsTime=1639830110'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
}
response = requests.get(url, headers=headers)

data = response.content

with open('天外来物.mp4', 'wb') as f:
    f.write(data)
