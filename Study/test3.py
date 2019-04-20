# -*- coding: utf-8 -*-
# @File  : test3.py
# @Author: 郭迎辉
# @Time  : 2019/3/29/02914:01
# @Desc  :
from bs4 import BeautifulSoup
from lxml import html
import xml
import requests

url = "https://movie.douban.com/chart"
f = requests.get(url)                 #Get该网页从而获取该html内容
soup = BeautifulSoup(f.content, "lxml")  #用lxml解析器解析该网页的内容, 好像f.text也是返回的html
for k in soup.find_all('div',class_='pl2'):#,找到div并且class为pl2的标签
   a = k.find_all('span')       #在每个对应div标签下找span标签，会发现，一个a里面有四组span
   print(a[0].string)
