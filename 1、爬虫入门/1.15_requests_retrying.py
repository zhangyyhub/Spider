# -*- coding: utf-8 -*-
# filename  : 1.15_requests_retrying.py
# datatime  : 2021/12/18 下午7:04
# author    : Yannic Zhang
# explain   : None

import random
import requests
from retrying import retry

proxy = ['175.146.96.90:4285', '42.228.120.185:4254', '125.111.144.142:4245']  # 代理IP池
rand = random.choice(proxy)    # 随机选择IP
proxies = {
    'http': 'http://{}'.format(rand)
}

# 用户代理
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'
}

# 尝试3次
@retry(stop_max_attempt_number=3)
def pare_url(url):
    response = requests.get(url, headers=headers, timeout=3, proxies=proxies)
    print(response.text)
    return response


pare_url('http://httpbin.org/get')
