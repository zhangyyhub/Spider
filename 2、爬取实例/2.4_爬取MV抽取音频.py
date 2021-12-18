# -*- coding: utf-8 -*-
# filename  : 2.4_爬取MV抽取音频.py
# datatime  : 2021/12/18 下午8:30
# author    : Yannic Zhang
# explain   : None

import requests
import os

url = 'https://mvwebfs.ali.kugou.com/202112182106/aed30b0dd6628f0c04ae91ae2e68893a/G249/M01/13/19/mYcBAF-2TO-AELasAQ_eJoyQWpk437.mp4'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
}
response = requests.get(url, headers=headers)

data = response.content

with open('稻香.mp4', 'wb') as f:
    f.write(data)

# 处理MV
os.system('ffmpeg -i 稻香.mp4 -vn -y -acodec copy 稻香.m4a')
