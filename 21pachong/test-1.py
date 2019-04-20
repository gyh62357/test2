# -*- coding: utf-8 -*-
# @File  : test-1.py
# @Author: 郭迎辉
# @Time  : 2019/4/8/00820:42
# @Desc  :学习前的准备
from urllib import request
from urllib import parse
#打开网页
# url = 'http://www.baidu.com'
# resp = request.urlopen(url)
# print(resp.read())

#下载网页或者图片
# request.urlretrieve('https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1554741197429&di=2769bbf2bc623c2cf9ceaec58804ef26&imgtype=0&src=http%3A%2F%2Fp0.qhimgs4.com%2Ft01f914d57356cfd1e2.jpg','E://1.jpg')

#urlencode 用法
# parms = {'name':'张三','age':'22'}
# result = parse.urlencode(parms)
# print(result)
#urlencode 用法
url = 'https://www.baidu.com/s'
pf = {'name':'郭迎辉'}
ps = parse.urlencode(pf)
url = url + '?' + ps
resp = request.urlopen(url)
print(resp.read())

#parse_qs  解码用法
# parms = {'name':'张三','age':'22'}
# result = parse.urlencode(parms)
# print(result)
# result2 = parse.parse_qs(result)
# print(result2)

#解析url,urlsplit没有params,基本上一模一样的
#url这样的url都可以获取到
url1 = 'http://www.baidu.com/s?wd=python&username=abc#1'
#url2中，只有urlparse可以获取hello
url = 'http://www.baidu.com/s;hello?wd=python&username=abc#1'
result1 = parse.urlsplit(url)
print(result1)
result = parse.urlparse(url)
print(result)
print('scheme:',result.scheme)
print('netloc:',result.netloc)
print('path:',result.path)
print('params:',result.params)
print('query:',result.query)


print('end')