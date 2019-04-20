# -*- coding: utf-8 -*-
# @File  : 322-1.py
# @Author: 郭迎辉
# @Time  : 2019/3/22/02210:18
# @Desc  :爬虫与反爬虫
#一级下拉词
# import requests
# import json
# keyword = '连衣裙'
# url = 'https://suggest.taobao.com/sug?q={}&code=utf-8&area=c2c'.format(keyword)
# html = requests.get(url)
# str_json = json.loads(html.text)
# for item in str_json['result']:
#     print(item[0])


#戴帽子反爬虫
#间隔数秒反爬虫
#更改ip反爬虫
import requests
import urllib.request
import json
# import time
keyword = '连衣裙'
keyword_encode = urllib.request.quote(keyword)
#反爬虫，带“帽子”
headers = {'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'}
#更改ip
proxies = {"http":"http://163.204.240.242"}
url = 'https://suggest.taobao.com/sug?q={}&code=utf-8&area=c2c'.format(keyword_encode)
html = requests.get(url,headers = headers,proxies = proxies)
str_json = json.loads(html.text)
for item in str_json['result']:
    url2 = 'https://suggest.taobao.com/sug?q={}&code=utf-8&area=c2c'.format(item[0])
    html2 = requests.get(url2)
    str_json2 = json.loads(html2.text)
    for item2 in str_json2['result']:
        print(item2[0])
        # time.sleep(2)






