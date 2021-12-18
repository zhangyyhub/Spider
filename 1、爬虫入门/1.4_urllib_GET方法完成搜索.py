# -*- coding: utf-8 -*-
# filename  : 1.4_urllib_GET方法完成搜索.py
# datatime  : 2021/12/18 下午4:46
# author    : Yannic Zhang
# explain   : None

from urllib.request import Request, urlopen
from urllib import parse
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

base_url = 'http://cn.bing.com/search'
d = {'q': '阿里云'}
u = parse.urlencode(d)
url = "{}?{}".format(base_url, u)

print(url)                   # http://cn.bing.com/search?q=%E9%98%BF%E9%87%8C%E4%BA%91
print(parse.unquote(url))    # http://cn.bing.com/search?q=阿里云

# 伪装
ua = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"
request_obj = Request(url, headers={
    'User-agent': ua
})

with urlopen(request_obj) as res:
    with open('aliyun.html', 'wb+') as f:    # save aliyun.html
        f.write(res.read())
        f.flush()
