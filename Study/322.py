# -*- coding: utf-8 -*-
# @File  : 322.py
# @Author: 郭迎辉
# @Time  : 2019/3/22/0229:57
# @Desc  :

import urllib.request
url = 'https://suggest.taobao.com/sug?q=liany&code=utf-8&area=c2c'
responce = urllib.request.urlopen(url)
html = responce.read()
html = html.decode('utf-8')
print(html)








