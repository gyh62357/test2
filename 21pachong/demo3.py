# -*- coding: utf-8 -*-
# @File  : demo3.py
# @Author: 郭迎辉
# @Time  : 2019/4/9/00920:55
# @Desc  : 使用cookie模拟登陆爬取
from urllib import request

#不使用cookie去请求主页
dapeng_url = 'http://www.renren.com/303827045/profile'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
           'Referer':'http://www.renren.com/303827045/profile',
           'Cookie':'an_slot=1719; anonymid=ju9sgotil0kygg; depovince=GW; _r01_=1; __utma=151146938.764976.1554814738.1554814738.1554814738.1; __utmz=151146938.1554814738.1.1.utmcsr=renren.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _de=15E098A46E81BF3F3399691954C56086696BF75400CE19CC; p=d1acb88094de2fb1846e1300963457805; ap=303827045; ln_uact=623575595@qq.com; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; jebe_key=d3b536c6-02b0-466c-ba82-9d0af710a151%7C5079ea02b04738720247a65bd5d9485f%7C1554814795566%7C1%7C1554814795748; first_login_flag=1; t=7436b1246d101c11bff7def2109eaa365; societyguester=7436b1246d101c11bff7def2109eaa365; id=303827045; xnsid=fadea6a1; XNESSESSIONID=69178678173c; wp_fold=0; ver=7.0; loginfrom=null'}
#返回一个请求对象
req = request.Request(url=dapeng_url,headers=headers)
#返回一个响应对象
resp = request.urlopen(req)
# print(resp.read().decode('utf-8'))
with open('renren1test10.html','w') as fp:
    #write函数必须写入一个str的数据类型
    #resp.read()读出来的是一个bytes数据类型
    #bytes -> decode -> str
    #str -> encode -> bytes
    fp.write(resp.content.decode('utf-8'))
    fp.close()
print('end')


