"""
用于读取数据的模块
"""
import pymysql
from items import params

class ReadData(object):
    #在初始化中连接数据库
    def __init__(self):
        dbparams = {
            'host': '127.0.0.1',
            'port': 3306,
            'user': 'root',
            'password': 'root',
            'database': 'pymysql_demo',
            'charset': 'utf8'
        }
        self.coon = pymysql.connect(**dbparams)
        self.cursor = self.coon.cursor()

    def read(self, file):
        length = len(params)
        sql = 'select '+(length-1)*'%s,' % (params[:-1]) + '%s' % params[-1] + ' from ' + file
        self.cursor.execute(sql)
        data = self.cursor.fetchall()

        return data

    def close(self):
        #关闭资源
        self.coon.close()