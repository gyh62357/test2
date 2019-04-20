# -*- coding: utf-8 -*-
# @File  : 314.py
# @Author: 郭迎辉
# @Time  : 2019/3/14/01421:54
# @Desc  :爬取豆瓣网


import requests
from lxml import html

url = 'https://movie.douban.com/'  # 需要爬数据的网址
page = requests.Session().get(url)
tree = html.fromstring(page.text)
result = tree.xpath('//td[@class="title"]//a/text()')  # 获取需要的数据
count = 0
for i in result:
    print(i, end='\\n')
    count += 1
    if (count % len(result) == 0):
        print(end='\\n')







