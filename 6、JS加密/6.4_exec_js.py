# -*- coding: utf-8 -*-
# filename  : 6.4_exec_js.py
# datatime  : 2021/12/23 下午1:41
# author    : Yannic Zhang
# explain   : None

import execjs

# 使用文件读写拿到js文件中的代码
with open("6.4_demo.js", "r+") as f:
    jsCode = f.read()
    # print(jsCode)

# js代码编码
js_obj = execjs.compile(jsCode)

# 执行js代码
res = js_obj.call("fn", 123)
print(res)
