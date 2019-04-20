# -*- coding: utf-8 -*-
# @File  : 321.py
# @Author: 郭迎辉
# @Time  : 2019/3/21/02121:11
# @Desc  :爬取图片

import urllib.request
import re

url = 'https://www.hc360.com/hots/900133437.html'
responce = urllib.request.urlopen(url)
html = responce.read()
# responce = urllib.request.Request(url)创建一个请求对象
# responce = urllib.request.urlopen(url)发送请求
html = html.decode('utf-8')
print('开始')
reg = r'src="(.+?\.jpg..220x220a.jpg)" class' #.+? 表示匹配一次或多次
imgre = re.compile(reg) #编译正则表达式，返回的是一个RegexObject对象，通过这个调用findall，match，search对象
imglist = re.findall(imgre,html)
x = 1000
for i in imglist:
    urllib.request.urlretrieve(i,'C:\\Users\\Administrator\\Desktop\\pic\\%d.jpg'%x)
    x +=1
print('end')

