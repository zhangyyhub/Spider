# -*- coding: utf-8 -*-
# filename  : 6.1_md5加密.py
# datatime  : 2021/12/21 上午8:27
# author    : Yannic Zhang
# explain   : None

import hashlib

data = 'abc123'
target1 = hashlib.md5(data.encode()).hexdigest()
print(type(target1), target1)   # <class 'str'> e99a18c428cb38d5f260853678922e03

target2 = hashlib.md5(data.encode()).digest()
print(type(target2), target2)   # <class 'bytes'> b'\xe9\x9a\x18\xc4(\xcb8\xd5\xf2`\x856x\x92.\x03'
