# -*- coding: utf-8 -*-
# filename  : 3.2_JSON数据解析.py
# datatime  : 2021/12/19 下午4:28
# author    : Yannic Zhang
# explain   : None

import json

p_data1 = {
    'person': [
        {
            'name': 'Tom',
            'age': 18
        },
        {
            'name': 'Jerry',
            'age': 17
        }
    ],
    'total': 2
}

j_data = json.dumps(p_data1)  # json字符串
print(type(j_data), j_data)   # <class 'str'> {"person": [{"name": "Tom", "age": 18}, {"name": "Jerry", "age": 17}], "total": 2}

p_data2 = json.loads(j_data)  # dict
print(type(p_data2), p_data2) # <class 'dict'> {'person': [{'name': 'Tom', 'age': 18}, {'name': 'Jerry', 'age': 17}], 'total': 2}


with open('test.json', 'w', encoding='utf-8') as f:
    json.dump(p_data1, f, ensure_ascii=False)

with open('test.json', 'r', encoding='utf-8') as f:
    p_data = json.load(f)
    print(type(p_data), p_data)
