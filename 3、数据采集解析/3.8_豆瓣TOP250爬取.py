# -*- coding: utf-8 -*-
# filename  : 3.8_豆瓣TOP250爬取.py
# datatime  : 2021/12/19 下午5:35
# author    : Yannic Zhang
# explain   : None

import requests
from lxml import etree
import json

url = "https://movie.douban.com/top250"

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
}

response = requests.get(url, headers=headers)
html = etree.HTML(response.text)
movie = html.xpath("//span[@class='title'][1]/text()")    # xpath工具中不写text()也会获取文本，但是代码中要写
movie_url = html.xpath("//div[@class='hd']/a[@class='']/@href")
target = dict(zip(movie, movie_url))
print(target)

with open("douban_top250.json", "w", encoding="utf-8") as f:
    json.dump(target, f, ensure_ascii=False)
