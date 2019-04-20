# -*- coding: utf-8 -*-
# @File  : qq.py
# @Author: 郭迎辉
# @Time  : 2018/11/29/02915:20
# @Desc  :
import pymysql
#连接数据库
conn = pymysql.connect(host = "localhost", user = "root", passwd = "123456")
#创建操作的游标
cursor = conn.cursor()
#选择数据库
conn.select_db('gyh')
#编写SQL语句
#sql = " insert into first (id,name) values(20,\"范昌盛\") "   #增加
#sql = " delete from first where id = 1"                    #删除
#sql = "update first set name = \"俄罗斯\" where id = 3 "  #改
sql = " select * from first"                           #查
#执行SQL并得到结果集
cursor.execute(sql)
#输出结果集 全部 cursor.fetchall()  单个cursor.fetchone()  多条cursor.fetchmany(n)
result = cursor.fetchall()
print(result)
# 关闭游标和连接
cursor.close()
conn.close()