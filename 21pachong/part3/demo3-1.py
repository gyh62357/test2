# -*- coding: utf-8 -*-
# @File  : demo3-1.py
# @Author: 郭迎辉
# @Time  : 2019/4/14/01410:05
# @Desc  :使用xml解析HTML
#1、解析html字符串，使用etree.html解析
#2、使用etree.html解析，这个函数默认的是xml解析器，如果碰到不规范的HTML，代码会解析错误，这个时候就要自己创建HTML解析器
from lxml import etree
text = """"""
#从text中读取html文件
def parse_text():
    htmlElement = etree.HTML(text)
    print(etree.tostring(htmlElement,encoding='utf-8').decode())
#直接从文件中读取
def parse_baidufile():
    htmlElement = etree.parse('tenxun.html')
    print(etree.tostring(htmlElement,encoding='utf-8').decode())
def parse_lagoufile():
    parser = etree.HTMLParser(encoding='utf-8')
    htmlElement = etree.parse('lagou.html',parser=parser)
    print(etree.tostring(htmlElement,encoding='utf-8').decode('utf-8'))
if __name__ == '__main__':
    parse_baidufile()









