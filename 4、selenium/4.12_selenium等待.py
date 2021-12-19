# -*- coding: utf-8 -*-
# filename  : 4.12_selenium等待.py
# datatime  : 2021/12/19 下午7:47
# author    : Yannic Zhang
# explain   : None

"""
强制等待：time.sleep()
隐式等待：会在设置时间内判断是否请求完成，完成进行下一步，没完成抛出超时加载
"""

from selenium import webdriver

chrome = webdriver.Chrome()
# 隐式等待
chrome.implicitly_wait(10)    # 最长设置20秒
chrome.get("https://www.baidu.com/")

chrome.find_element_by_id('lg')
