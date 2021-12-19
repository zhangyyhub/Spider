# -*- coding: utf-8 -*-
# filename  : 4.2_有界面模式.py
# datatime  : 2021/12/19 下午5:53
# author    : Yannic Zhang
# explain   : None

# 导包
from selenium import webdriver

# 创建浏览器对象
chrome = webdriver.Chrome()

# 发送请求
chrome.get("https://www.baidu.com/")

# 获取数据
data = chrome.page_source
print(type(data), data)    # str <html>...</html>
