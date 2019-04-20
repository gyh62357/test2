# -*- coding: utf-8 -*-
# @File  : demo3-2.py
# @Author: 郭迎辉
# @Time  : 2019/4/15/01520:56
# @Desc  :
from lxml import etree

parser = etree.HTMLParser(encoding='utf-8')
htmlElement = etree.parse('tenxun.html',parser=parser)
#1.获取所有tr标签
#//tr
#xpath 返回的是一个列表
# trs = htmlElement.xpath('//tr')
# for tr in trs:
#     print(etree.tostring(tr,encoding='utf-8').decode('utf-8'))
#2.获取第二个tr标签
# tr = htmlElement.xpath('//tr[2]')[0]
# print(etree.tostring(tr,encoding='utf-8').decode('utf-8'))
#3.获取所有class等于even的tr标签
# trs = htmlElement.xpath('//tr[@class="even"]')
# for tr in trs:
#     print(etree.tostring(tr, encoding='utf-8').decode('utf-8'))
#4.获取所有a标签的href属性
ahref = htmlElement.xpath('//a/@href')
for a in ahref:
    print(a)










