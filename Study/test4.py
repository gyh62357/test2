# -*- coding: utf-8 -*-
# @File  : test4.py
# @Author: 郭迎辉
# @Time  : 2019/3/30/0309:35
# @Desc  :
# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import numpy as np

def printP():
    global n
    global pieces
    for i in range(n):
        for j in range(n):
            print("%d\t" % pieces[i][j],)

def init():
    '''
    初始化棋盘
    '''
    global n
    global pieces
    global point  # 用于记录剩余的点
    pieces = [([0] * 100) for j in range(100)]
    pieces = np.array(pieces)

    point = []
    for i in range(n):
        for j in range(n):
            point.append((i, j))


def checkXY(x, y):
    '''
    检查点（x,y）是否在棋盘上
    '''
    global n
    if x >= 0 and x < n and y >= 0 and y < n:
        return True
    return False


def out1(x, y):
    '''
    找出所有方向（包括已经被走过的点）
    '''
    global n
    global pieces
    global direction
    outLine1 = []
    for i in range(8):
        x1 = x + direction[i][0]
        y1 = y + direction[i][1]
        if checkXY(x1, y1):
            outLine1.append((x1, y1))
    return outLine1


def out(x, y):
    '''
    找出所有可能走的路径
    '''
    outLine1 = out1(x, y)
    outLine = []
    for item in outLine1:
        if pieces[item[0]][item[1]] == 0:
            outLine.append(item)
    return outLine


def check1():
    '''
    剪枝1： 判断初始点各个方向上的点是否已经全走过
    '''
    global point
    global direction
    global x0
    global y0

    for i in range(8):
        x1 = x0 + direction[i][0]
        y1 = y0 + direction[i][1]
        if checkXY(x1, y1):
            if (x1, y1) in point:
                return True
    return False


def check2(x, y):
    '''
    判断剩余点中是否存在孤立点
    '''
    global point

    for p in point:
        if p[0] == x and p[1] == y:
            continue
        if len(out(p[0], p[1])) < 1:
            return True
    return True


def play(x, y, k):
    global n
    global x0, y0
    global succ
    global point

    pieces[x][y] = k

    point.remove((x, y))

    if k == n * n:  # 找到一条巡游路径
        if (x0, y0) in out1(x, y):  # 判断能否回到初始点
            succ = True
        return

    k += 1
    outLine = out(x, y)
    l = len(outLine)
    if l == 0:  # 该点没有出路回溯
        return
    else:
        outDic = dict()
        for item in outLine:
            outDic[item] = len(out(item[0], item[1]))
        # 按出路从小到达排序
        outDic = sorted(outDic.iteritems(), key=lambda d: d[1], reverse=False)

        for item in outDic:
            if check1() == False:
                continue
            if check2(x, y) == False:
                continue
            play(item[0][0], item[0][1], k)
            if succ:  # 如果已经找到则跳出循环
                break
            pieces[item[0][0], item[0][1]] = 0  # 还原步骤，继续搜索
            point.append((item[0][0], item[0][1]))
        return  # 搜索不到则回溯


if __name__ == "__main__":
    pieces = []  # 记录巡游顺序
    point = []  # 记录剩余的点
    direction = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]  # 八个方向
    succ = False

    n = 8  # 棋盘维n*n维

    # 起始点
    x0 = 1
    y0 = 1

    '''
    #控制台输入
    while checkXY(x0,y0)==False:
        print "左上角坐标为（0,0）"
        n = int(raw_input("n:").strip())
        x0 = int(raw_input("x0:").strip())
        y0 = int(raw_input("y0:").strip())
    '''
    print("n:", n)
    print("起始点:(%d,%d)\n" % (x0, y0))
    init()  # 初始化
    play(x0, y0, 1)  # 开始巡游

    if succ:
        print("找到一条巡游路径")
    else:
        print("不存在巡游路径")
