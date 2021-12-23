# -*- coding: utf-8 -*-
# filename  : 6.3_有道翻译.py
# datatime  : 2021/12/23 下午12:42
# author    : Yannic Zhang
# explain   : None

import requests
import hashlib
import time
import random
import jsonpath

url = "https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"


"""
# alt +enter
lts_ = str(int(time.time() * 1000))
salt_ = lts_ + str(random.randint(0, 9))
a = "fanyideskweb" + data_ + salt_ + "Y2FYu%TNSbMCxc3t2u^XT"
sign_ = hashlib.md5(a.encode()).hexdigest()
# alt + 鼠标左键'
form_data = {
    'i': data_,
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': salt_,
    'sign': sign_,
    'lts': lts_,
    'bv': '1d2b4167c633641e6ecd441258f686b5',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_CLICKBUTTION'
"""


# 输入
i = "hello"

# 时间戳
lts = str(int(time.time() * 1000))

# 随机数
salt = lts + str(random.randint(0, 9))

# sign
sign = hashlib.md5("fanyideskweb{}{}Y2FYu%TNSbMCxc3t2u^XT".format(i, salt).encode()).hexdigest()

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36",
    "Referer": "https://fanyi.youdao.com/",
    "Cookie": 'OUTFOX_SEARCH_USER_ID_NCOO=1818204335.4546208; OUTFOX_SEARCH_USER_ID="1793517384@10.108.160.19"; _ga=GA1.2.397748015.1630842275; JSESSIONID=aaaCr_I3rCcJUfXjWh7Ux; ___rl__test__cookies=1630939146446'
}

from_data = {
    "i": i,
    "from": "AUTO",
    "to": "AUTO",
    "smartresult": "dict",
    "client": "fanyideskweb",
    "salt": salt,
    "sign": sign,
    "lts": lts,
    "bv": "a914da195129fbf3e21e0ddc9662cd69",
    "doctype": "json",
    "version": "2.1",
    "keyfrom": "fanyi.web",
    "action": "FY_BY_REALTlME"
}

response = requests.post(url, headers=headers, data=from_data)
data = response.json()
fy = jsonpath.jsonpath(data, "$..tgt")[0]
print(fy)

"""
实时变化：需要模拟js加密
salt: 16309328636223
sign: 25e8f1e4c96e60b67ace37e057deda11
lts: 1630932863622

1、点击三个点
2、点击Search
3、搜索以上三个参数
4、点击文件
5、点击pretty
6、在Ctrl+f搜索以上三个参数
salt：
    ts: r,
    bv: t,
    r = "" + (new Date).getTime()               # 时间戳
    i = r + parseInt(10 * Math.random(), 10);   # 随机数

salt: i
sign: n.md5("fanyideskweb" + e + i + "Y2FYu%TNSbMCxc3t2u^XT")



# 时间戳
i = "hello"

t = time.time()
lt = str(int(t*1000))

# 随机数
sal = lt + str(random.randint(1, 9))

# sign
sig = hashlib.md5("fanyideskweb + {} + {} + Y2FYu%TNSbMCxc3t2u^XT".format(i, sal).encode()).hexdigest()
print(sig)

"fanyideskweb + i + i + Y2FYu%TNSbMCxc3t2u^XT"
# print(t)
# 1630934886.4529972
# 1630932863622
# 1630934946112
"""
