# -*- coding: utf-8 -*-
# @File  : 322-3.py
# @Author: 郭迎辉
# @Time  : 2019/3/22/02215:26
# @Desc  :二级下拉词
import requests
import urllib.request
import json
import pandas as pd
result = {'tielt':'title','level':'level'}
data = pd.DataFrame.from_dict(result,orient='index').T
data.to_csv("C:\\Users\\Administrator\\Desktop\\xlc.csv",index=False,header=False)#如果有mode=’a+’，
#则可以把之前文件里的内容清空
# import time
keyword = '连衣裙'
keyword_encode = urllib.request.quote(keyword)
#反爬虫，带“帽子”
headers = {'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'}
#更改ip
proxies = {"http":"http://163.204.240.242"}
url = 'https://suggest.taobao.com/sug?q={}&code=utf-8&area=c2c'.format(keyword_encode)
html = requests.get(url,headers = headers,proxies = proxies)
print(html.status_code == 200)#判断域名
str_json = json.loads(html.text)
for item in str_json['result']:
    result['title'] = item[0]
    result['level'] = 1
    data = pd.DataFrame.from_dict(result, orient='index').T
    data.to_csv("C:\\Users\\Administrator\\Desktop\\xlc.csv", index=False, header=False, mode='a+')
    url2 = 'https://suggest.taobao.com/sug?q={}&code=utf-8&area=c2c'.format(urllib.request.quote(item[0]))
    html2 = requests.get(url2)
    str_json2 = json.loads(html2.content.decode('utf-8'))
    for item2 in str_json2['result']:
        result['tielt'] = item2[0]
        result['level'] = 2
        data = pd.DataFrame.from_dict(result, orient='index').T
        data.to_csv("C:\\Users\\Administrator\\Desktop\\xlc.csv",index=False,header=False,mode='a+')













