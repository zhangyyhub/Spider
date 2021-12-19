# -*- coding: utf-8 -*-
# filename  : 4.13_京东图书案例.py
# datatime  : 2021/12/19 下午7:50
# author    : Yannic Zhang
# explain   : None

"""
获取小说书名：//div[@class='p-name']/a[@target='_blank']/em
获取小说价格：//strong/i/text()
"""

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import Options
from lxml import etree
import time

url = "https://list.jd.com/list.html?cat=1713%2C3258&shop=1&click=1"

options = Options()
options.add_argument("--headless")
# chrome = webdriver.Chrome(options=options)
chrome = webdriver.Chrome()
# 设置主页渲染时间，5秒之后不管有没有渲染完毕，代码继续执行
chrome.set_page_load_timeout(10)
try:
    chrome.get(url)
except Exception:
    print("主页渲染超时")

for i in range(1, 10):
    n = 1000 * i
    time.sleep(1)
    chrome.execute_script("document.documentElement.scrollTop={}".format(n))

data = chrome.page_source
# print(data)

html = etree.HTML(data)
bookname = html.xpath("//div[@class='p-name']/a[@target='_blank']/em/text()")
bookprice = html.xpath("//strong/i/text()")

targ = dict(zip(bookname, bookprice))
print(len(targ), targ)

"""
滑动鼠标查看书的数量变多了（60本）
所以我们需要先滑动，再去获取网页源代码
"""