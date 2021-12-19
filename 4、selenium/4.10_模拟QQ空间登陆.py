# -*- coding: utf-8 -*-
# filename  : 4.10_模拟QQ空间登陆.py
# datatime  : 2021/12/19 下午7:29
# author    : Yannic Zhang
# explain   : None

"""
模拟QQ空间登陆:
1、创建浏览器对象
2、发送请求
3、定位到"账号密码登陆"并点击
4、定位到"账号"并点击，之后输入账号
5、定位到"密码"并点击，之后输入密码
6、定位到"登陆"并点击
"""

# from selenium import webdriver
# import time
#
# url = "https://qzone.qq.com/"
#
# chrome = webdriver.Chrome()
# chrome.get(url)
#
# time.sleep(2)
# chrome.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
# """
# selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: {"method":"xpath","selector":"//*[@id="switcher_plogin"]"}
# 报错！
# 原因：这个登陆页面是在另一个URL中(嵌套页面)
# """
#
# chrome.quit()


from selenium import webdriver
import time

url = "https://qzone.qq.com/"

chrome = webdriver.Chrome()
chrome.get(url)

time.sleep(2)
# 定位到frame元素
frome = chrome.find_element_by_xpath('//*[@id="login_frame"]')
# 切换到定位的frame标签页的页面中
chrome.switch_to.frame(frome)
# 点击使用账号密码登陆
chrome.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
# 定位账号密码框并输入
chrome.find_element_by_xpath('//*[@id="u"]').send_keys("******")
chrome.find_element_by_xpath('//*[@id="p"]').send_keys("******")

# 登陆
chrome.find_element_by_xpath('//*[@id="login_button"]').click()

time.sleep(2)
chrome.quit()
