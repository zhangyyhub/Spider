# -*- coding: utf-8 -*-
# filename  : 3.3_JSONPATH模块.py
# datatime  : 2021/12/19 下午4:44
# author    : Yannic Zhang
# explain   : None

import jsonpath

data = {'商店': {
    '书': [
        {'类别': '参考',
         '作者': '奈杰尔·里斯',
         '标题': '世纪语录',
         '价格': 8.95
         },
        {'category': 'fiction',
         'author': 'Evelyn Waugh',
         'title': 'Sword of Honor',
         'price': 12.99
         },
        {'类别': '小说',
         '作者': '赫尔曼·梅尔维尔',
         '标题': '白鲸记',
         'isbn': '0-553-21311-3',
         '价格': 8.99
         },
        {'类别': '小说',
         '作者': 'JRR 托尔金',
         '标题': '指环王',
         'isbn': '0-395-19395-8',
         '价格': 22.99
         }
    ],
    '自行车': {
        '颜色': '红色',
        '价格': 19.95
    }
}
}

# 获取商店的值
print(1, jsonpath.jsonpath(data, '$.商店'))       # [{'书': [...], '自行车': {...}}]

# 获取书的值
print(2, jsonpath.jsonpath(data, '$.商店.书'))    # [[{}, {}, {}]]

# 获取书的所有值
print(3, jsonpath.jsonpath(data, '$.商店.书.*'))  # [{}, {}, {}]

# 获取书的所有值(递归)
print(4, jsonpath.jsonpath(data, '$..书.*'))      # [{}, {}, {}]

# 获取第三本书的信息
print(5, jsonpath.jsonpath(data, '$..书[2]'))

# 获取前两本书的信息
print(6, jsonpath.jsonpath(data, '$..书[0,1]'))   # 包前包后
print(7, jsonpath.jsonpath(data, '$..书[0:2]'))   # 包前不包后

# 获取最后一本书的信息
print(8, jsonpath.jsonpath(data, '$..书[(@.length-1)]'))    # ()支持表达式计算

# 获取'作者的所有值'
print(9, jsonpath.jsonpath(data, '$..书[?(@.标题)]'))    # 此处中文获取不到
print(10, jsonpath.jsonpath(data, '$..书[?(@.isbn)]'))   # 英文就可以获取

# 获取价格大于10的所有书
print(11, jsonpath.jsonpath(data, '$..书[?(@.price > 10)]'))
