# -*- coding: utf-8 -*-
# @File  : demo1.py
# @Author: 郭迎辉
# @Time  : 2019/4/9/0099:32
# @Desc  : 爬取拉勾网，戴帽子爬取
from urllib import request,parse
#response url
url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
#带上帽子反 反爬虫
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
           'Referer': 'https://www.lagou.com/jobs/list_python?city=%E5%85%A8%E5%9B%BD&cl=false&fromSearch=true&labelWords=&suginput=',
           }
data = {
    'first':'true',
    'pn':1,
    'kd':'python'
}
#data进行encode编码，再转换为python能识别的utf-8编码，再进行解码
response = request.Request(url,headers=headers,data=parse.urlencode(data).encode('utf-8'),method='POST')
resp = request.urlopen(response)
#进行解码
print(resp.read().decode('utf-8'))







