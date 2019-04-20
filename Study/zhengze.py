# -*- coding: utf-8 -*-
# @File  : zhengze.py
# @Author: 郭迎辉
# @Time  : 2019/3/27/02720:39
# @Desc  : 正则表达式
# re.match() 当且仅当匹配的字符串在开头，才能匹配到
#re.findall()返回列表
#re.search()精确匹配，匹配字符要在前面,匹配数字按从大到小的顺序写

#
import requests
from bs4 import BeautifulSoup
import re
url = 'http://www.cthy.com/'
strhtml = requests.get(url)
soup = BeautifulSoup(strhtml.text,'lxml')
soup = soup.select('#newsList_qy > li:nth-of-type(4) > a:nth-of-type(2)')
for item in soup:
    result = {
        'title':item.get_text(),
        'link':item.get('href'),
        'ID':re.findall(r'\d+',item.get('href'))
    }
    print(result)
# print(re.search(r'\.','he love 2.you'))
print(re.search(r'\d{2}','i love 123 cad.com'))
print(re.search(r'\d{3}\.\d{3}\.\d{3}\.\d{3}','113.231.144.134'))
print(re.search(r'\d+\.\d+\.\d+\.\d+','113.231.14.4'))
#创建字符类[],只要匹配到字符类里面的任何一个都可以
print(re.search(r'[eiou]','i love cd.com.ou'))

print(re.search(r'\d{9}@qq\.com','623575595@qq.com'))

