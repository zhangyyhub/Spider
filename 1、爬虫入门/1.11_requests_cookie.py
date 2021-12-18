# -*- coding: utf-8 -*-
# filename  : 1.11_requests_cookie.py
# datatime  : 2021/12/18 下午6:20
# author    : Yannic Zhang
# explain   : None

# import requests
#
# # 登陆状态的豆瓣网页
# url = 'https://www.douban.com/gallery/'
#
# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'}
# cookies = {'Cookie': 'll="118172"; bid=Cg8KVjc4lW0; __gads=ID=42d97db0e73ac2c3-229bee94bfca0061:T=1628516986:RT=1628516986:S=ALNI_MZ8GXcLnY_7qb7GaTtloo3iNYl_xg; ap_v=0,6.0; __utmc=30149280; dbcl2="251780356:R7AYYmRBPrQ"; ck=Lmb4; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1639822768%2C%22https%3A%2F%2Faccounts.douban.com%2F%22%5D; _pk_ses.100001.8cb4=*; push_noty_num=0; push_doumail_num=0; __utma=30149280.1719341592.1627194672.1639818046.1639822769.15; __utmz=30149280.1639822769.15.8.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmt=1; __utmv=30149280.25178; _pk_id.100001.8cb4=7d131909fd5e6485.1627646863.3.1639822880.1627898680.; __utmb=30149280.14.10.1639822769'}
#
# response = requests.get(url, headers=headers, cookies=cookies)
#
# data = response.content
#
# with open('douban_logging.html', 'wb') as f:
#     f.write(data)


import requests

# 登陆状态的豆瓣网页
url = 'https://www.douban.com/gallery/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
    'Cookie': 'll="118172"; bid=Cg8KVjc4lW0; __gads=ID=42d97db0e73ac2c3-229bee94bfca0061:T=1628516986:RT=1628516986:S=ALNI_MZ8GXcLnY_7qb7GaTtloo3iNYl_xg; ap_v=0,6.0; __utmc=30149280; dbcl2="251780356:R7AYYmRBPrQ"; ck=Lmb4; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1639822768%2C%22https%3A%2F%2Faccounts.douban.com%2F%22%5D; _pk_ses.100001.8cb4=*; push_noty_num=0; push_doumail_num=0; __utma=30149280.1719341592.1627194672.1639818046.1639822769.15; __utmz=30149280.1639822769.15.8.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmt=1; __utmv=30149280.25178; _pk_id.100001.8cb4=7d131909fd5e6485.1627646863.3.1639822880.1627898680.; __utmb=30149280.14.10.1639822769',
}

response = requests.get(url, headers=headers)

data = response.content

with open('douban_logging.html', 'wb') as f:
    f.write(data)
