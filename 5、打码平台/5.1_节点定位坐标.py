# -*- coding: utf-8 -*-
# filename  : 5.1_节点定位坐标.py
# datatime  : 2021/12/20 下午9:14
# author    : Yannic Zhang
# explain   : None

from selenium import webdriver
import time

chrome = webdriver.Chrome()
chrome.get("https://www.baidu.com/")
time.sleep(2)
chrome.maximize_window()

# 定位百度图片
img = chrome.find_element_by_xpath('//*[@id="s_lg_img_new"]')
# 获取左上角坐标
location = img.location
print(location)    # {'x': 585, 'y': 44}
# 获取图片的宽高
size = img.size
print(size)        # {'height': 129, 'width': 270}
# 右下角的坐标
x = location['x'] + size['width']
y = location['y'] + size['height']
print(x, y)        # 855 173


time.sleep(2)
chrome.quit()
