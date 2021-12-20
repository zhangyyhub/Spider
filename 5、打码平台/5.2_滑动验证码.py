# -*- coding: utf-8 -*-
# filename  : 5.2_滑动验证码.py
# datatime  : 2021/12/20 下午9:40
# author    : Yannic Zhang
# explain   : None

from selenium import webdriver
import time

# 创建一个浏览器对象
chrome_obj = webdriver.Chrome()

# 发送请求
chrome_obj.get("https://www.helloweba.net/demo/2017/unlock/")

# 1.定位按钮
click_obj = chrome_obj.find_element_by_class_name("slide-to-unlock-handle")

# 2.按住滑块
# 创建一个动作链对象，参数就是浏览器对象
action_obj = webdriver.ActionChains(chrome_obj)
# 点击并且按住，参数就是定位的按钮
action_obj.click_and_hold(click_obj)
# 得到他的宽高
size_ = click_obj.size
width_ = size_['width']
print(size_)
# 3.定位滑动坐标
action_obj.move_by_offset(width_, 0).perform()

# 4.松开滑动
action_obj.release()


time.sleep(4)
chrome_obj.quit()
