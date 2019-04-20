# -*- coding: utf-8 -*-
# @File  : 322-2.py
# @Author: 郭迎辉
# @Time  : 2019/3/22/02213:43
# @Desc  :二级下拉词

import requests
import json
import urllib.request
keyword = '连衣裙'
# keyword = urllib.request.quote(keyword)
url = 'https://suggest.taobao.com/sug?q={}&code=utf-8&area=c2c'.format(keyword)
html = requests.get(url)
str_json = json.loads(html.text)
for item in str_json['result']:
    url2 = 'https://suggest.taobao.com/sug?q={}&code=utf-8&area=c2c'.format(item[0])
    html2 = requests.get(url2)
    str_json2 = json.loads(html2.text)
    for item2 in str_json2['result']:
        print(item2[0])
