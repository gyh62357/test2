# -*- coding: utf-8 -*-
# @File  : ni.py
# @Author: 郭迎辉
# @Time  : 2018/12/5/00521:29
# @Desc  :
import numpy as np

# 逆时针内螺旋矩阵
def interSpiralMatrix(size):
    if (size % 2 != 1):  # size必须是奇数
        size += 1
    #spiralMatrix = [([0] * size) for i in range(size)]  # 生成矩阵
    spiralMatrix = np.zeros([size, size], int)  # 生成0矩阵
    x, y, side = int(size / 2), int(size / 2), size - 1  # x,y先初始化为中心点1的坐标，side表示边长
    # 生成坐标系，游标i通过判断坐标所属的区域来判断坐标应该进行的变化
    for i in range(1, size ** 2 + 1):  # 坐标的变化是 x++ , y --, x--, y++,,,i 表示所有的值
        spiralMatrix[y][x] = i
        if (y >= -x + side and y >= x):    # 划分四个区域（分别为x++ , y --, x--, y++的区域），然后就是通过直线来分开
            x += 1
        elif(-x + side < y and y < x):
            y -= 1
        elif(y <= -x+side and y < x):
            x -= 1
        elif(y >= x and y < -x+side):
            y += 1

    for matrix in spiralMatrix:
        print("\t".join(map(lambda x : str(x), matrix)))
    #print(spiralMatrix)
interSpiralMatrix(11)