# -*- coding: utf-8 -*-
# filename  : 4.8_反检测.py
# datatime  : 2021/12/19 下午7:08
# author    : Yannic Zhang
# explain   : None

import time
from selenium import webdriver

url = "https://www.baidu.com/"

options = webdriver.ChromeOptions()
# 添加参数进行隐藏
options.add_experimental_option('excludeSwitches', ['enable-automation'])

# 创建浏览器对象
chrome = webdriver.Chrome(options=options)

# 发送请求
chrome.get(url)

# 定位搜索框
input_obj = chrome.find_element_by_id("kw")

# 点击搜索框
input_obj.click()

# 输入内容
input_obj.send_keys("薛之谦")

# 定位搜索按钮并点击
find_obj = chrome.find_element_by_id("su")
find_obj.click()

time.sleep(2)
chrome.close()
chrome.quit()
