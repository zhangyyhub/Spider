# -*- coding: utf-8 -*-
# filename  : 4.4_元素定位方法.py
# datatime  : 2021/12/19 下午5:57
# author    : Yannic Zhang
# explain   : Element positioning method

from selenium import webdriver

chrome = webdriver.Chrome()

chrome.find_element_by_id()
chrome.find_element_by_name()
chrome.find_element_by_class_name()
chrome.find_element_by_tag_name()
chrome.find_element_by_link_text()
chrome.find_element_by_partial_link_text()
chrome.find_element_by_xpath()
chrome.find_element_by_css_selector()
