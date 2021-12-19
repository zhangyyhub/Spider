# -*- coding: utf-8 -*-
# filename  : 3.7_HTML数据提取.py
# datatime  : 2021/12/19 下午5:27
# author    : Yannic Zhang
# explain   : None

from lxml import etree

data = """
<div><ul>
    <li class="item-1"><a href="link1.html">first item</a></li>
    <li class="item-1"><a href="link2.html">second item</a></li>
    <li class="item-inactive"><a href="link3.html">shird item</a></li>
    <li class="item-1"><a href="link4.html">fourth item</a></li>
    <li class="item-0"><a href="link5.html">fifth item</a></li>
</ul></div>
"""

html = etree.HTML(data)
print(type(html), html)

bytesData = etree.tostring(html)  # 获取bytes类型
print(type(bytesData), bytesData)

strData = bytesData.decode()      # bytes类型解码
print(type(strData), strData)

print(html.xpath("//li[@class='item-1']/a/@href"), html.xpath("//li[@class='item-1']//text()"))
target = dict(zip(html.xpath("//li[@class='item-1']/a/@href"), html.xpath("//li[@class='item-1']//text()")))
print(target)
