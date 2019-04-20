# -*- coding: utf-8 -*-
# @File  : 407.py
# @Author: 郭迎辉
# @Time  : 2019/4/7/00710:48
# @Desc  :
import sys
import numpy as np

board=np.zeros((8,8))
def print_board(start_x,start_y):
    if traval(start_x,start_y)==1:
        print ("success\n")
        for i in range(board.shape[0]):
            for j in range(board.shape[1]):
                print ("%c%d"%(' ',int(board[i][j])),end=' ')
                pass
            print('\n')
            pass
        pass
    pass

def traval(x,y):
    #可移动的八个方向
    move_x=np.array([-2, -1, 1, 2, 2, 1, -1, -2])
    move_y=np.array([1, 2, 2, 1, -1, -2, -2, -1 ])

    #下一步的位置坐标
    next_i=np.zeros(8)
    next_j=np.zeros(8)

    #出处个数
    exit_out=np.zeros(8)
    i,j=x,y
    board[int(i)][int(j)]=1
    for m in range(2,65):
        for n in range(8):
            exit_out[n]=0
            pass
        n=0
        for k in range(8):
            temp_i=int(i)+move_x[k]
            temp_j=int(j)+move_y[k]
            if temp_i<0 or temp_j<0 or temp_i>7 or temp_j>7:
                continue
            if board[int(temp_i)][int(temp_j)]==0:
                next_i[n]=temp_i
                next_j[n]=temp_j
                n+=1
                pass
            pass
        count=n
        if count==0:
            return 0
        elif count==1:
            min_=0
            pass
        else:
            #记录下一个位置的出处数目
            for n in range(count):
                for k in range(8):
                    temp_i=next_i[n]+move_x[k]
                    temp_j=next_j[n]+move_y[k]
                    if temp_i<0 or temp_j<0 or temp_i>7 or temp_j>7:
                        continue
                    if board[int(temp_i)][int(temp_j)]==0:
                        exit_out[n]+=1
                        pass
                    pass
                pass
            min_=0
            temp=exit_out[0]
            for n in range(count):
                if temp>exit_out[n]:
                    temp=exit_out[n]
                    min_=n
                    pass
                pass
            pass

        i=next_i[min_]
        j=next_j[min_]
        board[int(i)][int(j)]=m
        pass
    return 1

if __name__=="__main__":
    start_x=sys.argv[1]
    start_y=sys.argv[2]
    print_board(start_x,start_y)
