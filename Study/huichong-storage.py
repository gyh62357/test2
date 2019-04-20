# -*- coding: utf-8 -*-
# @File  : huichong-storage.py
# @Author: 郭迎辉
# @Time  : 2019/3/30/03010:32
# @Desc  : 存储数据

import pandas as pd
result = {'tielt':'title','level':'level'}
data = pd.DataFrame.from_dict(result,orient='index').T
data.to_csv("C:\\Users\\Administrator\\Desktop\\xlc.csv",index=False,header=False)#如果有mode=’a+’，
#则可以把之前文件里的内容清空
for item in range(100):
    data = pd.DataFrame.from_dict(item, orient='index').T
    data.to_csv("C:\\Users\\Administrator\\Desktop\\xlc.csv", index=False, header=False)
