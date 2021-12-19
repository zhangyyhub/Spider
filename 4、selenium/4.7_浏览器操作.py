# -*- coding: utf-8 -*-
# filename  : 4.7_浏览器操作.py
# datatime  : 2021/12/19 下午6:05
# author    : Yannic Zhang
# explain   : None

"""
1. 控制浏览器窗口大小
    driver.set_window_size(480, 800)

2. 浏览器后退，前进
    后退: driver.back()
    前进: driver.forward()

3. 刷新
    driver.refresh()

4. 关闭页面
    chrome.close()

5. 退出浏览器
    chrome.quit()

6. 获取当前页面的url
    current_url

7. 通过定位获取的标签对象的text属性，获取文本内容
    element.text

8. 通过定位获取的标签对象的get_attribute函数，传入属性名，来获取属性的值
    element.get_attribute("属性名")

9. 滚动页面
    window.scrollTo(横向x轴,竖向y轴)，可以执行像素单位进行移动
    window.scrollTo(0,document.body.scrollHeight)，可以以页面为单位进行移动
    document.documentElement.scrollTop=2000，到达指定的坐标单位

10. 执行js代码
    driver.execute_script(js)
"""
