# -*- coding: utf-8 -*-
# @File  : laoshu.py
# @Author: 郭迎辉
# @Time  : 2019/4/8/00810:37
# @Desc  :走迷宫
import sys
# 用来判断坐标是否合法
def check_valid(mg, x, y):
    if x >= 0 and x < len(mg) and y >= 0 and y < len(mg[0]) \
            and mg[x][y] == 1:
        return True
    else:
        return False


# 迷宫结果优化
def process(step):
    # 先识别哪些无路可走的点的下一个点
    change_records = []
    for i in range(len(step) - 1):
        if (abs(step[i][0] - step[i + 1][0]) == 0 and abs(step[i][1] - step[i + 1][1]) == 1) or \
                (abs(step[i][0] - step[i + 1][0]) == 1 and abs(step[i][1] - step[i + 1][1]) == 0):
            pass
        else:
            change_records.append(i + 1)
    # print(change_records)

    # 然后根据这些点识别出这个点的最远回退点
    clip_nums = []
    for i in change_records:
        for j in range(i):
            if (abs(step[j][0] - step[i][0]) == 0 and abs(step[j][1] - step[i][1]) == 1) or \
                    (abs(step[j][0] - step[i][0]) == 1 and abs(step[j][1] - step[i][1]) == 0):
                break
        clip_nums.append((j, i))
    # print(clip_nums)

    # 注意回退点之间的包含关系, 逆序处理, 是为了规避顺序对列表进行处理后下标偏移的问题
    record = []
    for i in clip_nums[::-1]:
        if not (i[0] in record or i[1] in record):
            step = step[:i[0] + 1] + step[i[1]:]
        record += list(range(i[0], i[1]))
    print(step)


step = []


def walk(mg, x, y):
    global step
    if x == 0 and y == 0:
        step.append((x, y))
        process(step)
        print("Walk success!")
        sys.exit()

    if check_valid(mg, x, y):
        step.append((x, y))
        mg[x][y] = 2
        walk(mg, x, y + 1)
        walk(mg, x, y - 1)
        walk(mg, x - 1, y)
        walk(mg, x + 1, y)


mg = [[1, 0, 1, 1, 1, 0],
      [1, 1, 1, 0, 1, 1],
      [0, 0, 0, 1, 0, 1],
      [0, 1, 1, 1, 0, 1],
      [0, 1, 0, 1, 1, 1],
      [1, 1, 1, 0, 0, 0]]

walk(mg, 5, 0)  # 从5, 0这个点开始走迷宫, 出口为0, 0
