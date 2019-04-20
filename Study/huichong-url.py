# -*- coding: utf-8 -*-
# @File  : huichong-url.py
# @Author: 郭迎辉
# @Time  : 2019/3/30/03010:23
# @Desc  : 提取url
import requests
import re
from bs4 import BeautifulSoup
url = 'https://www.hc360.com/hots-pr8/900233034.html'
responce = requests.get(url)
soup = BeautifulSoup(responce.content,'lxml')
# print(soup)
reg = r'href="(.+?\.html)" onclick' #.+? 表示匹配一次或多次
href = re.compile(reg)
href_list = re.findall(href,soup.decode('utf-8'))
x = 0
for i in href_list:
    print(i)
    x += 1
print(x)
