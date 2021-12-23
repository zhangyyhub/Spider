# -*- coding: utf-8 -*-
# filename  : 6.5_baidufanyi_js.py
# datatime  : 2021/12/23 下午2:03
# author    : Yannic Zhang
# explain   : None

"""
from: en
to: zh
query: hello
transtype: realtime
simple_means_flag: 3
sign: 54706.276099
token: df6af41d8362570a7c1671c0672a3a96
domain: common

from: en
to: zh
query: word
transtype: realtime
simple_means_flag: 3
sign: 924944.720417
token: df6af41d8362570a7c1671c0672a3a96
domain: common

1.查看网页源码
    搜索sign
2.分析源码
    发现函数复杂不好模仿，则使用PyExecJS去执行代码
"""

import requests
import execjs
import jsonpath

url = "https://fanyi.baidu.com/v2transapi?from=en&to=zh"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36",
    "Referer": "https://fanyi.baidu.com/",
    "Cookie": 'PSTM=1627024921; BAIDUID=DB39528E8812B10A4E76036BA8733708:FG=1; BIDUPSID=4412AED8223BE100976308ADF2B96C24; __yjs_duid=1_be4affe4227c5671b89a8b652f3d3d931627041919573; BDUSS=1zRkJJLUdHSXBaRzFGYlpJfnBLVVN0ekRGYkNDSHl4N1cybU1JVDZsNkRuakZoSVFBQUFBJCQAAAAAAAAAAAEAAACm~PqvQWFuMjMyMTEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIMRCmGDEQphbS; BDUSS_BFESS=1zRkJJLUdHSXBaRzFGYlpJfnBLVVN0ekRGYkNDSHl4N1cybU1JVDZsNkRuakZoSVFBQUFBJCQAAAAAAAAAAAEAAACm~PqvQWFuMjMyMTEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIMRCmGDEQphbS; BAIDUID_BFESS=DB39528E8812B10A4E76036BA8733708:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1631435389,1631435399; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1631435407; __yjs_st=2_MWM3Njc2YmM1Njk5MDk3MWIwMTQ2NmMwNDgwMzE1ODZkM2YyYWMwNjNjODZhODk0NjY5YWFmMWRlYzZiMzY5NzUxMzU0YTFhZDEzNzJiZDg5YmY4NGY0NTRhMDlhMjdlNjMwMzJkMjRkMTI0OTcyM2JkYTBiY2ZjZDc2NDkzYTM0NTNiNzQzZjQ4NTQ0MDZjNDc4MjRlMzVkNWI1Y2EyOTBlMjkzM2VmMzM1NTc0ODdkMTM4MjM1NmU0ZTcwNDZmYzk1Yjc4MjMzNmY3Nzc0OGYzOGY2NjMzZTQxNjhhNjYwMGY4ZGFhMGIwZTNiOTdjYWJkOWNiMDliNzdiYzY5M183X2MwYWE1NTc0; ab_sr=1.0.1_ZDFkODA5MjBhYzY4YTA1Y2E0OGVlMTgwYzUyYmU0ZDEyOWVlODY4ZGI0YzEyM2E1MGU5NmM3MmMwZjlmZTAxYTY1MmM3MDc5ZGQ0M2MyZDAxNDg2YzE4Y2RjOWFkMTZiYmZlMmY3N2ZhZjk1M2U4YTFkOGYwOTk1NjQ3MjI3NjU5MmRmNTQ0OWIwNmE4NmI4ZTI3M2ExZDQwYWJjYTVjNDBjZTc0YTZmODA5NjlhYzVjNDljNDlmYjkwMjljNjdk'
}

inputData = input("请输入英文：")

with open("6.5_baidufanyi.js", "r") as f:
    jsData = f.read()

jsObj = execjs.compile(jsData)

sign = jsObj.call("e", inputData)

fromData = {
    "from": "en",
    "to": "zh",
    "query": inputData,
    "transtype": "realtime",
    "simple_means_flag": "3",
    "sign": sign,
    "token": "df6af41d8362570a7c1671c0672a3a96",
    "domain": "common"
}

response = requests.post(url, headers=headers, data=fromData)
pyData = response.json()
# print(type(pyData), pyData)
target = jsonpath.jsonpath(pyData, "$..dst")
print(target[0])

"""
报错1：i没有被定义
    execjs._exceptions.ProgramError: ReferenceError: i is not defined
    解决方法：打断点
    u = i = "320305.131321201"    # 静态数据

报错2：n没有被定义
    execjs._exceptions.ProgramError: ReferenceError: n is not defined
"""