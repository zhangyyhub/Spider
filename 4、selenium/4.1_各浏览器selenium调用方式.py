# -*- coding: utf-8 -*-
# filename  : 4.1_各浏览器selenium调用方式.py
# datatime  : 2021/12/19 下午5:50
# author    : Yannic Zhang
# explain   : None

from selenium import webdriver

# Firefox浏览器
driver1 = webdriver.Firefox()
driver2 = webdriver.Firefox("驱动路径")

# Chrome浏览器
driver3 = webdriver.Chrome()

# Internet Explorer浏览器
driver4 = webdriver.Ie()

# Edge浏览器
driver5 = webdriver.Edge()

# Opera浏览器
driver6 = webdriver.Opera()


# 打开网页
driver1.get('urllink')
