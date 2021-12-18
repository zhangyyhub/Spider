# -*- coding: utf-8 -*-
# filename  : 1.7_urllib_https证书忽略.py
# datatime  : 2021/12/18 下午5:41
# author    : Yannic Zhang
# explain   : None

import ssl    # 导入ssl模块
from urllib.request import Request, urlopen

# request_obj = Request('http://www.12306.cn/mormhweb/')  # 可以访问
# request_obj = Request('https://www.baidu.com/')         # 可以访问
request_obj = Request('https://www.12306.cn/mormhweb/')   # 报SSL认证异常

request_obj.add_header(
    'User-agent',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
)

# 忽略不信任的证书: 可以忽略不校验的上下文
context = ssl._create_unverified_context()

with urlopen(request_obj, context=context) as res:
    print(res._method)
    print(res.read())
