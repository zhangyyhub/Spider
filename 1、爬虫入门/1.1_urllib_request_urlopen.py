# -*- coding: utf-8 -*-
# filename  : 1.1_urllib_request_urlopen.py
# datatime  : 2021/12/18 下午3:24
# author    : Yannic Zhang
# explain   : None

from urllib.request import urlopen

url = 'http://www.bing.com'
response = urlopen(url, timeout=5)

print(response.closed)                          # False

with response:
    print(1, type(response))                    # http.client.HTTPResponse类文件对象
    print(2, response.status, response.reason)  # 状态
    print(3, response.geturl())                 # 返回真正的URL
    print(4, response.info())                   # headers
    print(5, response.read())                   # 读取返回的内容
    print(6, response._method)                  # GET方法

print(response.closed)                          # True
