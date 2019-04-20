# -*- coding: utf-8 -*-
# @File  : huichongwang.py
# @Author: 郭迎辉
# @Time  : 2019/3/30/0308:43
# @Desc  : 慧聪网数据爬取
import requests
from bs4 import BeautifulSoup
from lxml import html
import xml
import re


url = 'https://b2b.hc360.com/supplyself/589368909.html'
f = requests.get(url)
soup = BeautifulSoup(f.content,'lxml')

for info_company in soup.find_all('div',class_ = 'p sate'):#(L)
    company_name = info_company.find_all('em')
    print('公司名称',company_name[0].string)
for info_product in soup.find_all('div',class_ = 'proTitCon'):#(L)
    product_name = info_product.find_all('h1')
    print('产品名称：',product_name[0].string)
for info_price in soup.find_all('div',class_ = 'topPriceBox '):#(L)
    product_price = info_price.find_all('div')
    price = ''.join(product_price[0].string.split())
    print('产品报价：',price)
for info_name in soup.find_all('div',class_ = 'p name'):#(L)
    name = info_name.find_all('em')
    print('联系人',name[0].string)
for info_iPhone in soup.find_all('div',class_ = 'p tel2'):#(L)
    iPhone = info_iPhone.find_all('span')
    iPhone_num = info_iPhone.find_all('em')
    print(iPhone[0].string,iPhone_num[0].string)
