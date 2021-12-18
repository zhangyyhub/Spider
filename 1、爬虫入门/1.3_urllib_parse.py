# -*- coding: utf-8 -*-
# filename  : 1.3_urllib_parse.py
# datatime  : 2021/12/18 下午4:12
# author    : Yannic Zhang
# explain   : None

from urllib import parse

# example 1
u = parse.urlencode({
    'id': 1,
    'name': 'tom',
})
print(u)    # id=1&name=tom


# example 2
"""
get method
url = 'http://www.bing.com/?id=1&name=tom'

post method
url = 'http://www.bing.com/'
body = 'id=1&name=tom'
"""
u = parse.urlencode({
    'id': 1,
    'name': 'tom',
    'url': 'http://www.bing.com/?id=1&name=tom',
})
print(u)    # id=1&name=tom&url=http%3A%2F%2Fwww.bing.com%2F%3Fid%3D1%26name%3Dtom


# example 3
u = parse.urlencode({
    'id': 1,
    'name': '张三',
    'url': 'http://www.bing.com/?id=1&name=张三',
})
print(u)    # id=1&name=%E5%BC%A0%E4%B8%89&url=http%3A%2F%2Fwww.bing.com%2F%3Fid%3D1%26name%3D%E5%BC%A0%E4%B8%89


# example 3
# 网页使用utf-8编码
# https://www.baidu.com/s?wd=中，编码后为：https://www.baidu.com/s?wd=%E4%B8%AD

u = parse.urlencode({'wd': '中'})    # 编码 ——> wd=%E4%B8%AD
url = "https://www.baidu.com/s?{}".format(u)
print(url)                     # https://www.baidu.com/s?wd=%E4%B8%AD

# 编码
print('中'.encode('utf-8'))    # b'\xe4\xb8\xad'
# 解码
print(parse.unquote(u))        # wd=中
print(parse.unquote(url))      # https://www.baidu.com/s?wd=中
