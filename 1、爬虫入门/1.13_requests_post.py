# -*- coding: utf-8 -*-
# filename  : 1.13_requests_post.py
# datatime  : 2021/12/18 下午6:32
# author    : Yannic Zhang
# explain   : None

import requests

url = 'https://www.tuicool.com/login'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
    'cookie': 'UM_distinctid=17ae2b71b4e19-0c179840ccffbb-35637203-13c680-17ae2b71b4fac6; CNZZDATA5541078=cnzz_eid%3D1937101849-1639816777-https%253A%252F%252Fwww.tuicool.com%252F%26ntime%3D1639816777; _tuicool_session=QjU4WnQrRmt5cjNyU2hDeVpBd1h2TFRzMzJpMEtMaVVPWXI0YnhYQU5qbWUzV1E5cWVpWHY0TWdzN2IzcHNndzhUZEFpakdLNFVXVFY0T0VmYUt4T1FES1pJQ01neUx5YnkwTE9aRkRVQzFGSGRaV1pGUEJraVpyalFFS1BwaTVsdmpKYVNVbWVXaU5peW5lMUk0bHMzaVN4dFpqZW1tNUx0aDVXbEZhQVZPTGNndENqNDVOVnQwN2pRaVAvSGNDa3R1bzdGd21VN28vR29CcisvUDNPZUZzUjVvRndjTmdCSXUyMkdjeUFWdVZFQjZ2SVhuamNEVTc5amUyZnNQNXpCdFBZeS9ndWRDTXNSK1dEVUMxYzhkVGVBU2FFYlY5SHJNZy84YnNLS3BNT01KNUlUcThQZDhpZUJkQzFPbGJEczV3VkxxUlM4WSs2RUVZeHN4c0h3PT0tLVA2OHZBaGdTa0N5dHhSbWQxRE9hVEE9PQ%3D%3D--556d7e98718cea8de9f713468d49b2c314a6344f',
}

data = {
    'authenticity_token': '9Ol6T9lO7ucbyzO3wZel57IXf37HCt5KfQP8IHCEbtbr7GgJLBIhMEl0MdavTe8UWRfGwHBd4/jhyOG2hQg77A==',
    'email': '*****',
    'password': '*****',
}


response = requests.post(url, headers=headers, data=data)

data = response.content

with open('tuicool_login.html', 'wb') as f:
    f.write(data)
