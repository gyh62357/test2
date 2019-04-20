# -*- coding: utf-8 -*-
# @File  : demo8.py
# @Author: 郭迎辉
# @Time  : 2019/4/11/01114:50
# @Desc  : request使用代理ip
import requests
proxy = {
    'http':'125.123.121.32:9000'
}
response = requests.get('http://httpbin.org/ip',proxies=proxy)
print(response.text)




