# -*- coding: utf-8 -*-
# filename  : XML数据提取.py
# datatime  : 2021/12/19 下午5:11
# author    : Yannic Zhang
# explain   : None

from lxml import etree

string = """
<bookstore>
<book>
  <title lang="eng">Harry Potter</title>
  <price>29.99</price>
</book>

<book>
  <title lang="eng">Learning XML</title>
  <price>39.95</price>
</book>

</bookstore>
"""

xml = etree.XML(string)

# 获取根元素bookstore
print(1, xml.xpath("/bookstore"))            # [<Element bookstore at 0x7fa2a27f3050>]

# 获取bookstore子元素的所有book元素
print(2, xml.xpath("/bookstore/book"))       # [<Element book at 0x7fd43626dbe0>, <Element book at 0x7fd43626db90>]

# 获取所有book的子元素
print(3, xml.xpath("//book/*"))              # [<Element title at 0x7fd43626dbe0>, <Element price at 0x7fd43626db90>, <Element title at 0x7fd43626db40>, <Element price at 0x7fd43626daf0>]

# 获取属于bookstore元素后代的所有book元素
print(4, xml.xpath("/bookstore//book"))      # [<Element book at 0x7fd43626dbe0>, <Element book at 0x7fd43626db90>]

# 获取lang属性值为eng的所有title元素
print(5, xml.xpath("//title[@lang='eng']"))  # [<Element title at 0x7fe9c426cc80>, <Element title at 0x7fe9c426cc30>]

# 获取属于bookstore子元素的第一个book元素的title文本,注意下标从1开始
print(6, xml.xpath("/bookstore/book[1]/title/text()"))       # ['Harry Potter']

# 获取属于bookstore子元素的最后一个book元素的title文本,注意下标从1开始
print(7, xml.xpath("/bookstore/book[last()]/title/text()"))  # ['Learning XML']

# 获取bookstore下面的book元素的title文本，从第二个开始
print(8, xml.xpath("/bookstore/book[position()>1]/title/text()"))  # ['Learning XML']

# 获取所有book下的title元素，仅仅选择文本为'Harry Potter'的文本
print(9, xml.xpath("//book/title[text()='Harry Potter']/text()"))  # ['Harry Potter']

# 获取bookstore元素中的book元素的所有title文本，且其中price元素的值大于35
print(10, xml.xpath("/bookstore/book[price>35]/title/text()"))     # ['Learning XML']

# 获取bookstore元素的所有子元素
print(11, xml.xpath("/bookstore/*"))  # [<Element book at 0x7fc91826ccd0>, <Element book at 0x7fc91826cc80>]

# 获取所有带属性的title元素
print(12, xml.xpath("//title[@*]"))   # [<Element title at 0x7fb4c3a6cc80>, <Element title at 0x7fb4c3a6cc30>]

# 选取book元素的所有title元素和price元素
print(13, xml.xpath("//book/title | //book/price"))
