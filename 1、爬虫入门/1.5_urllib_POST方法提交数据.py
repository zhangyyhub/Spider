# -*- coding: utf-8 -*-
# filename  : 1.5_urllib_POST方法提交数据.py
# datatime  : 2021/12/18 下午4:52
# author    : Yannic Zhang
# explain   : None

from urllib.request import Request, urlopen
from urllib.parse import urlencode
import json

request_obj = Request('http://httpbin.org/post')
request_obj.add_header(
    'User-agent',
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"
)

data = urlencode({'name': '张三', 'age': '18'})
print(data)

# POST方法,From提交数据,不做url编码会有风险
with urlopen(request_obj, data=data.encode()) as res:
    print(res.read())

