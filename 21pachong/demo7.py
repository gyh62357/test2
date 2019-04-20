# -*- coding: utf-8 -*-
# @File  : demo7.py
# @Author: 郭迎辉
# @Time  : 2019/4/10/01022:13
# @Desc  :post请求
import requests
import json
proxy = {
    'http':'119.102.25.15:9999'
}
data = {
    'first':'true',
    'pn':'1',
    'kw':'python'
}
headers = {
    'Referer':'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
}
response = requests.post('https://www.lagou.com/jobs/positionAjax.json?xl=%E7%A1%95%E5%A3%AB&hy=%E7%A7%BB%E5%8A%A8%E4%BA%92%E8%81%94%E7%BD%91&px=default&city=%E6%B7%B1%E5%9C%B3&needAddtionalResult=false',data=data,headers=headers,proxies=proxy)
print(response.json())
print(response.text)

