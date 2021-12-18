# -*- coding: utf-8 -*-
# filename  : 1.2_urllib_request_Request.py
# datatime  : 2021/12/18 下午3:48
# author    : Yannic Zhang
# explain   : None

from urllib.request import urlopen, Request
import random
import ssl


url = 'http://www.bing.com/'

ua_list = [
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
]

# 全局取消证书验证。
# 可以通过常见的受信任证书成功验证，所以你最好不要试图绕过证书验证，而是要修复它。
ssl._create_default_https_context = ssl._create_unverified_context
# 构造request对象
request_obj = Request(url)

request_obj.add_header('User-agent', random.choice(ua_list))    # pick one
print(type(request_obj))                                        # <class 'urllib.request.Request'>

response = urlopen(request_obj, timeout=5)                      # url or request_object
print(type(response))                                           # <class 'http.client.HTTPResponse'>

with response:
    print(1, response.status, response.getcode(), response.reason)    # 状态，getcode本质就是返回status
    print(2, response.geturl())                                       # 返回数据的url，如果重定向，这个url和原来url不一样
    print(3, response.info())                                         # 返回响应头headers
    print(4, response.read())                                         # 读取返回的内容

print(5, request_obj.get_header('User-agent'))                  # Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11

