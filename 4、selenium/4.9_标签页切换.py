# -*- coding: utf-8 -*-
# filename  : 4.9_标签页切换.py
# datatime  : 2021/12/19 下午7:16
# author    : Yannic Zhang
# explain   : None

from selenium import webdriver
import time

# 创建浏览器对象
chrome = webdriver.Chrome()

# 发送请求
chrome.get("https://www.baidu.com/")

# 定位搜索框并点击
chrome.find_element_by_partial_link_text("hao").click()

# 切换回百度一下的窗口
windows = chrome.window_handles      # 获取当前所有标签页句柄构成的列表
time.sleep(2)
chrome.switch_to.window(windows[0])  # 根据句柄索引下标进行切换
time.sleep(2)
chrome.switch_to.window(windows[1])  # 根据句柄索引下标进行切换
time.sleep(2)
chrome.switch_to.window(windows[0])  # 根据句柄索引下标进行切换

# 退出浏览器
chrome.quit()
