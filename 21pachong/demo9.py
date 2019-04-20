# -*- coding: utf-8 -*-
# @File  : demo9.py
# @Author: 郭迎辉
# @Time  : 2019/4/11/01120:18
# @Desc  : request处理cookie信息
#如果想要多次使用cookie，那么应该使用session
import requests
proxy = {
    'http':'139.199.153.25:1080'
}
data = {
    'LoginID': 'gyh623575595',
    'password': 'gyh62357'}
url = 'https://sso.hc360.com/ssologin'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'}
session = requests.Session()
re = session.get(url,data=data,headers=headers,proxies=proxy)
response = session.get('http://home.hc360.com/homes/main/index.html')
with open('1234567890test.html','w',encoding='utf-8') as fp:
    fp.write(re.text)



