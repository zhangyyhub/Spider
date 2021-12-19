# -*- coding: utf-8 -*-
# filename  : 4.3_无界面模式.py
# datatime  : 2021/12/19 下午5:56
# author    : Yannic Zhang
# explain   : None

# 导包
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 实例化options对象
options = Options()
options.add_argument("--headless")

# 创建浏览器对象
chrom = webdriver.Chrome(options=options)

# 发送请求
chrom.get("https://www.baidu.com/")

# 获取数据
data = chrom.page_source
print(type(data), data)    # str <html>...</html>
