# -*- coding: utf-8 -*-
# @File  : zhonglvwang.py
# @Author: 郭迎辉
# @Time  : 2019/3/26/02617:11
# @Desc  : 中国旅游网
#使用beautifulSoup解析网页并抓取数据
# import requests
# import json
# from bs4 import BeautifulSoup
# url = 'http://www.cthy.com/'
# strhtml = requests.get(url)
# soup = BeautifulSoup(strhtml.text,'lxml')
# #一句css selector路径位置，寻找唯一的特征。
# # css选择器，soup.select()函数，返回的是list类型
# #通过绝对路径查找数据，标签+属性，方法copy select
# soup = soup.select('#newsList_qy > li > a:nth-of-type(2)')
# for item in soup:
#     result = {
#         'title':item.get_text(),
#         'link':item.get('href')
#     }
#     print(result)

import requests
import json
from bs4 import BeautifulSoup
url = 'https://news.sina.com.cn/china/'
strhtml = requests.get(url)
soup = BeautifulSoup(strhtml.text,'lxml')
#一句css selector路径位置，寻找唯一的特征。
# css选择器，soup.select()函数，返回的是list类型
#通过绝对路径查找数据，标签+属性，方法copy select
soup = soup.select('body > div:nth-of-type(12) > div.right-content > ul.news-2')
# soup = soup.select('#newsList_qy > li:nth-of-type(4) > a:nth-of-type(2)')
# soup = soup.select('#corMessageDialog > div > div.word-box')
print(soup)
for item in soup:
    result = {
        'title':item.get_text(),
        'link':item.get('href')
    }
    print(result)