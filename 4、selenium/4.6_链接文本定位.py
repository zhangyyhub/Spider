# -*- coding: utf-8 -*-
# filename  : 4.6_链接文本定位.py
# datatime  : 2021/12/19 下午6:03
# author    : Yannic Zhang
# explain   : None

from selenium import webdriver

url = "https://www.baidu.com/"

# 创建浏览器对象
chrome = webdriver.Chrome()

# 发送请求
chrome.get(url)

# 精准定位hao123
# chrome.find_element_by_link_text("hao123").click()

# 模糊定位hao123
chrome.find_element_by_partial_link_text("hao").click()
