# -*- coding: utf-8 -*-
# @File  : test2.py
# @Author: 郭迎辉
# @Time  : 2019/4/16/01616:58
# @Desc  :
import pandas as pd
from sklearn import  linear_model

df=pd.DataFrame({'weight':[51,53,54,55,57,60,62,65,69,72],'height':[152,156,160,164,168,172,176,180,184,188]})
X=pd.DataFrame(df['weight'])

y=df['height']
clf = linear_model.LinearRegression()
clf.fit(X, y)
print('回归系数: ', clf.coef_)
y_pred =clf.predict(X)
print(y_pred)
print(X,'\n',y)
# import matplotlib.pyplot as plt
# plt.scatter(X, y,  color='red') #真实值散点图

# plt.plot(X,y_pred, color='blue', linewidth=1.5) #线性回归预测趋势线

# plt.show()
print('test')
print('test')
