# -*- coding: utf-8 -*-
# @File  : test.py
# @Author: 郭迎辉
# @Time  : 2019/4/16/0169:32
# @Desc  :
import numpy as np
from numpy import random
from anqing import connectionsql
import pandas as pd
#m代表行，n代表列
m,n = np.shape(connectionsql.resList)
a = connectionsql.resList
print(m)
print(n)
for i in range(1,3):
    print('强力','棉结','条干','单强','毛羽')
    print(a[i][40],a[i][41],a[i][42],a[i][43],a[i][44])
#数据存到Excel中
#数据存到Excel中
# df = pd.DataFrame(connectionsql.resList)
# df.to_excel("C://Users//Administrator//Desktop//test//data.xlsx")






