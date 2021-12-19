# -*- coding: utf-8 -*-
# filename  : 4.11_cookie处理.py
# datatime  : 2021/12/19 下午7:41
# author    : Yannic Zhang
# explain   : None

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import Options

options = Options()
options.add_argument("--headless")

chrome = webdriver.Chrome(options=options)

chrome.get("https://www.baidu.com/")

# print(chrome.get_cookies())

# 转换为name,value作为键值对的cookie字典
cookie = {}
for i in chrome.get_cookies():
    cookie[i['name']] = i['value']
print(cookie)

# 删除一条cookie
chrome.delete_cookie('BA_HECTOR')
cookie1 = {}
for i in chrome.get_cookies():
    cookie1[i['name']] = i['value']
print(cookie1)

# 删除所有cookie
chrome.delete_all_cookies()
cookie2 = {}
for i in chrome.get_cookies():
    cookie2[i['name']] = i['value']
print(cookie2)

chrome.quit()
