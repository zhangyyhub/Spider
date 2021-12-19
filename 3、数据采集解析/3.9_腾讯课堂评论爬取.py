# -*- coding: utf-8 -*-
# filename  : 3.9_腾讯课堂评论爬取.py
# datatime  : 2021/12/19 下午5:38
# author    : Yannic Zhang
# explain   : None

import requests
import jsonpath
import json

url = "https://ke.qq.com/cgi-bin/comment_new/course_comment_list?cid=134017&count=10&page=0&filter_rating=0&bkn=1508709708&r=0.4223521937388812"

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
    'cookie': 'pgv_pvid=1137038448; fqm_pvqid=3d6ccae7-dc42-4c2d-a784-b1f2c5d4bf2f; tvfe_boss_uuid=7ca361dd0ee31f7c; pgv_info=ssid=s3075350362; _pathcode=0.9469249054386444; tdw_auin_data=-; iswebp=1; tdw_first_visited=1; ts_refer=www.baidu.com/link; ts_uid=1289956252; Hm_lvt_0c196c536f609d373a16d246a117fd44=1628954864; ptui_loginuin=1611748256; uin=o1611748256; skey=@KNC2sXkgL; RK=ayBIrri7YL; ptcz=acbd86ded6d4047b8f9b888ab607eb607b91135dc1ff687931fbf537397781cd; luin=o1611748256; lskey=00010000d24999efeeb4832c688b525c9a51e33438098e2641467217a210095c5f238fa5459a8095379f6094; pt4_token=oII4BsAPo2uJeLHOC2kOowHHx*TrEdBxq2z*cfmvnyk_; p_skey=0At2O1j*ZjAQOnvOcgAW2eI0aQ8*6XPgDJrvgMAMHg8_; p_lskey=000400004b6b1a78c1aa1e9f7fb1a7fd70be688c9f009b6837cf36ec0a543cbd135ff400c5a5f93c71bfa76d; auth_version=2.0; mix_login_mode=true; uid_type=0; uin=1611748256; p_uin=1611748256; p_luin=1611748256; uid_uin=1611748256; uid_origin_uid_type=0; ke_login_type=1; localInterest=[2056,2001]; index_new_key={"index_interest_cate_id":2056}; tdw_data_sessionid=162895492195118633530577; tdw_data={"ver4":"www.baidu.com","ver5":"","ver6":"","refer":"www.baidu.com","from_channel":"","path":"dh-0.9469249054386444","auin":"-","uin":1611748256,"real_uin":"611748256"}; tdw_data_testid=; tdw_data_flowid=; ts_last=ke.qq.com/course/134017; sessionPath=162895493647550137369814; Hm_lpvt_0c196c536f609d373a16d246a117fd44=1628954937; tdw_data_new_2={"auin":"-","sourcetype":"","sourcefrom":"","ver9":1611748256,"uin":1611748256,"visitor_id":"18623954480755156","sessionPath":"162895493647550137369814"}',
    'referer': 'https://ke.qq.com/course/list/python%E9%A9%AC%E5%93%A5'
}

response = requests.get(url, headers=headers)

# json——>dict方式一：
# data = json.loads(response.text)
# # print(data)

# json——>dict方式二：
data = response.json()
# print(type(data), data)

# 解析数据
nick_name = jsonpath.jsonpath(data, "$..nick_name")
first_comment = jsonpath.jsonpath(data, "$..first_comment")
# print(nick_name, first_comment)
target = dict(zip(nick_name, first_comment))
print(target)