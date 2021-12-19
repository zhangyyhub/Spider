# -*- coding: utf-8 -*-
# filename  : 4.5_实现百度搜素.py
# datatime  : 2021/12/19 下午6:00
# author    : Yannic Zhang
# explain   : None

from selenium import webdriver

url = "https://www.baidu.com/"

# 创建浏览器对象
chrome = webdriver.Chrome()

# 发送请求
chrome.get(url)

# 定位搜索框
input_obj = chrome.find_element_by_xpath('//*[@id="kw"]')
# input_obj = chrome.find_element_by_id("kw")
# input_obj = chrome.find_element_by_name("wd")
# input_obj = chrome.find_element_by_class_name("s_ipt")
# input_obj = chrome.find_element_by_css_selector("#kw")

# 点击搜索框
input_obj.click()

# 输入内容
input_obj.send_keys("python")

# 定位搜索按钮并点击
search_obj = chrome.find_element_by_id("su")
search_obj.click()
