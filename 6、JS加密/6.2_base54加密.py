# -*- coding: utf-8 -*-
# filename  : 6.2_base54加密.py
# datatime  : 2021/12/23 下午12:26
# author    : Yannic Zhang
# explain   : None


import base64

data = "abc123"

target1 = base64.b64encode(data.encode()).decode()
print(type(target1), target1)   # <class 'str'> YWJjMTIz
target2 = base64.b64decode(target1.encode()).decode()
print(type(target2), target2)   # <class 'str'> abc123
