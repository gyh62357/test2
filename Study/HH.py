# -*- coding: utf-8 -*-
# @File  : HH.py
# @Author: 郭迎辉
# @Time  : 2018/11/29/02910:26
# @Desc  :
from pylab import *
import matplotlib.lines
import numpy as np
x = np.linspace(-np.pi, np.pi, 26, endpoint=True)  #x的取值，最小值、最大值、样本点数
y = np.cos(x)
y1 = np.sin(x)
plot(x, y, '-.')
plot(x, y1)
title("Functions $\sin$ and $\cos$", color = "r")    #标题
xlim(-3.0, 3.0)     #x轴的上下限
ylim(-1.0, 1.0)     #y轴的上下限
#x轴上具体的坐标值，设置坐标轴刻度
xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi], [r'$-pi$', r'$-pi/2$', r'$0$', r'$pi/2$', r'$pi$'])
#y轴上具体的坐标值
yticks([-1, 0, 1], [r'$-1$', r'$0$', r'$1$'])
show()

