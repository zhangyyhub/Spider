# -*- coding: utf-8 -*-
# filename  : 5.3_超级鹰验证码.py
# datatime  : 2021/12/20 下午10:11
# author    : Yannic Zhang
# explain   : None

from selenium import webdriver
from PIL import Image

url = "https://www.chaojiying.com/user/login/"
# 创建浏览器对象
chrome = webdriver.Chrome()
# 发送请求
chrome.get(url)
# 窗口最大化
chrome.maximize_window()
# 页面截图
chrome.save_screenshot("login.png")
# 获取坐标
img = chrome.find_element_by_xpath("/html/body/div[3]/div/div[3]/div[1]/form/div/img")
location = img.location
# 获取图片大小
size = img.size
x1 = location['x']
y1 = location['y']
x2 = location['x'] + size['width']
y2 = location['y'] + size['height']

# 读取图片
img_ = Image.open("login.png")
# 裁剪图片
res_ = img_.crop((x1, y1, x2, y2))
res_.save("cjy.png")
