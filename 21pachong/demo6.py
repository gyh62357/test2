# -*- coding: utf-8 -*-
# @File  : demo6.py
# @Author: 郭迎辉
# @Time  : 2019/4/10/01021:16
# @Desc  :熟悉request库
import requests
params = {
    'wd':'郭迎辉'
}
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'}
response = requests.get('http://www.baidu.com/s',params=params,headers=headers)
with open('baidu5.html','w',encoding='utf-8') as fp:
    fp.write(response.content.decode())
print(response.url)

#content 直接从网络上抓取数据，没有经过任何编码，所以是一个bytes类型，其实在硬盘上和在网络上传输的字符串都是bytes类型
print(type(response.content))
#text 这个是str数据类型，是request库将content 进行解码的字符串。解码需要指定一个编码方式，request会根据自己的猜测来判断编码方式。所以有时候回产生错误。应该使用response.content.decode('utf-8')进行手动解码。
# print(response.text)
# print(response.url)
# print(response.encoding)
# print(response.status_code)
# response = requests.get('http://www.baidu.com'))








