# -*- coding: utf-8 -*-
# @File  : demo4.py
# @Author: 郭迎辉
# @Time  : 2019/4/10/01016:49
# @Desc  :
from urllib import request,parse
from http.cookiejar import CookieJar
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
    'Referer': 'http://www.renren.com/303827045/profile'}

def get_opener():
    #1、登陆
    #1.1 创建一个cookiejar对象
    cookiejar = CookieJar()
    #1.2使用cookiejar创建一个HTTPCookieProcess对象
    handler = request.HTTPCookieProcessor(cookiejar)
    #1.3使用上一步创建的handler创建一个opener
    opener = request.build_opener(handler)
    return opener

def login_renren(opener):
    #1.4使用opener发送登陆的请求（人人网的邮箱和密码）

    data = {
        'email':'623575595@qq.com',
        'password':'gyh62357'}
    login_url = 'http://www.renren.com/PLogin.do'
    # login_url = 'http://www.renren.com/SysHome.do'
    req = request.Request(login_url,data=parse.urlencode(data)
                          .encode('utf-8'),headers=headers)
    # request.urlopen(req)
    opener.open(req)

def visit_profile(opener):
    #2.访问个人主页
    dapeng_url = 'http://www.renren.com/303827045/profile'
    #获取个人主页的页面的时候，不要新建一个opener
    #而应该使用之前的那个opener，因为之前的那个opener已经包含了
    #登录所需要的cookie信息
    req = request.Request(dapeng_url,headers=headers)
    resp = opener.open(req)
    with open('renren_test1.html','w',encoding='utf-8') as fp:
        fp.write(resp.read().decode('utf-8'))

if __name__ == '__main__':
    opener = get_opener()
    login_renren(opener)
    visit_profile(opener)