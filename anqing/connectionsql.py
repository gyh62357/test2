# -*- coding: utf-8 -*-
# @File  : connectionsql.py
# @Author: 郭迎辉
# @Time  : 2019/4/16/01617:45
# @Desc  :
import pymssql
import pandas as pd
conn = pymssql.connect(host="127.0.0.1:1433", user="sa", password="123456", database="HZL09", charset="utf8")
#获取光标
cur = conn.cursor()
if not cur:
    raise (NameError,"数据库连接失败")
#conn.commit,可以从数据库中删除。否则只能打印的时候删除，增删改都需要
#插入数据
# sql1 = "insert into test values(89,'爱因斯坦')"
# cur.execute(sql1)
# conn.commit()
# #批量插入数据，注意要把"int"转化为"str"
# for i in range(0,20):
#     str_i = str(i)
#     sql1 = "insert into test values(" + str_i + ",'郑州轻工业大学')"
#     cur.execute(sql1)
#     conn.commit()
# #删除
# sql2 = "delete from test where name='郭'"
# cur.execute(sql2)
# conn.commit()
# #改写
# sql3 = "update test set id=2,name='牛顿' where id=1"
# cur.execute(sql3)
# conn.commit()

x=('F1', 'F2', 'F3')
# 查找,结果按照id排序
sql4 = 'select '+ 2*'%s,'%x[:-1]+'%s'%x[-1] +' from Sheet1'
print(sql4)
cur.execute(sql4)
resList = cur.fetchall()#fetchall()是接收全部的返回结果行
conn.close()
print(resList[0])
print('test successful')
print('test again')
print('test again')
print('test again')
print('test again')
print('test again')
print('test again')
print('test again')
print('last test')
print('ok')
print('last')
print('last')
print('last')
print('last')