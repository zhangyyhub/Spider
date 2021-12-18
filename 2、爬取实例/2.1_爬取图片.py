# -*- coding: utf-8 -*-
# filename  : 2.1_爬取图片.py
# datatime  : 2021/12/18 下午8:07
# author    : Yannic Zhang
# explain   : None

import requests

url = 'http://up.deskcity.org/pic/202010/dt/th5csfytliz2011.jpg'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
}

response = requests.get(url, headers=headers)

data = response.content

with open('photo.jpg', 'wb') as f:
    f.write(data)
