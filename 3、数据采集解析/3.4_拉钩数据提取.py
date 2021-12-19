# -*- coding: utf-8 -*-
# filename  : 3.4_拉钩数据提取.py
# datatime  : 2021/12/19 下午4:52
# author    : Yannic Zhang
# explain   : None

import json
import jsonpath
import requests

url = 'http://www.lagou.com/lbs/getAllCitySearchLabels.json'

# 用户代理
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'
}

# 发送请求获取响应
response = requests.get(url, headers=headers)

# json字符串
json_str = response.text

# 将json字符串转换成python类型
dict_data = json.loads(json_str)

# 提取数据获取城市
jsonpath_data = jsonpath.jsonpath(dict_data, '$..name')
print(type(jsonpath_data), jsonpath_data)

# 保存数据
# python数据类型转换成json数据
json_data = json.dumps(jsonpath_data, ensure_ascii=False)
with open('city1.json', 'w', encoding='utf-8')as f:
    f.write(json_data)

# python数据类型转换成json类型并且写入文件
with open('city2.json', 'w', encoding='utf-8')as f:
    json.dump(jsonpath_data, f, ensure_ascii=False)
