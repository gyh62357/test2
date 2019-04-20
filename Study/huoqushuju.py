# -*- coding: utf-8 -*-
# @File  : huoqushuju.py
# @Author: 郭迎辉
# @Time  : 2019/3/30/03010:54
# @Desc  :
import requests
import re
from bs4 import BeautifulSoup
import csv
print('正在爬取中，请稍候...')
#第一步获取某个类别中的若干个地址，例如榨油机
url1 = 'https://s.hc360.com/?w=%E6%A6%A8%E6%B2%B9%E6%9C%BA&mc=seller'#大类中的小类地址，只改变这一个就可以了，不过这也是一个可以改进的地方
responce = requests.get(url1)
soup = BeautifulSoup(responce.content,'lxml')
# print(soup)
reg = r'href="(.+?\.html)" onclick' #.+? 表示匹配一次或多次
href = re.compile(reg)
href_list = re.findall(href,soup.decode('utf-8'))
#定于全局变量
hcw_company_name = 0    #慧聪网公司名称
hcw_product_name = 0    #慧聪网产品名称
hcw_price = 0   #慧聪网报价
hcw_name = 0    #慧聪网联系人
hcw_iPhone = 0  #慧聪网联系人电话
#第二步得到具体产品的地址，爬取具体产品的信息
for url2 in href_list:
    # print(url2)
    lis = 'http:'
    url3 = lis + url2
    # print(url3)
    f = requests.get(url3)
    soup = BeautifulSoup(f.content, 'lxml')#用lxml解析器解析该网页的内容, 好像f.text也是返回的html
    for info_company in soup.find_all('div', class_='p sate'):  # (L)#,找到div并且class为p state的标签
        company_name = info_company.find_all('em')#在每个对应div标签下找em标签，然后根据自己所需要的进行取
        hcw_company_name = company_name[0].string
        # print('公司名称', hcw_company_name)
    for info_product in soup.find_all('div', class_='proTitCon'):  # (L)
        product_name = info_product.find_all('h1')
        hcw_product_name = product_name[0].string
        # print('产品名称：', hcw_product_name)
    for info_price in soup.find_all('div', class_='topPriceBox '):  # (L)
        product_price = info_price.find_all('div')
        hcw_price = product_price[0].string
        # print('产品报价：', hcw_price)
    for info_name in soup.find_all('div', class_='p name'):  # (L)
        name = info_name.find_all('em')
        hcw_name = name[0].string
        # print('联系人', hcw_name)
    for info_iPhone in soup.find_all('div', class_='p tel2'):  # (L)
        iPhone = info_iPhone.find_all('span')
        iPhone_num = info_iPhone.find_all('em')
        hcw_iPhone = iPhone_num[0].string
        # print(hcw_iPhone)
        # print(iPhone[0].string, iPhone_num[0].string)
    #第三步开始存储数据
    with open("C:\\Users\\Administrator\\Desktop\\huichongwang\\test3.csv", 'a',encoding='utf-8') as fw:
        writer = csv.writer(fw)
        writer.writerow([hcw_company_name,#公司名称
                         hcw_product_name,#产品名称
                         hcw_price, #产品报价
                         hcw_name,#联系人
                         hcw_iPhone,#手机号
                         url3  #地址
                         ])
    hcw_company_name = 0
print('end')

