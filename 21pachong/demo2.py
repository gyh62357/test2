# -*- coding: utf-8 -*-
# @File  : demo2.py
# @Author: 郭迎辉
# @Time  : 2019/4/9/00914:34
# @Desc  :使用ip代理器
from urllib import request
#不使用用代理
url = 'http://httpbin.org/ip'
resp = request.urlopen(url)
print(resp.read())
#使用代理
url = 'http://httpbin.org/ip'
#1、使用ProxyHandler，传入代理构建一个handler
handler = request.ProxyHandler({"http":"116.209.55.225:9999"})
#2、使用上面创建的handler构建一个opener
opener = request.build_opener(handler)
#3、使用opener去发送一个请求
resp = opener.open(url)
print(resp.read())




