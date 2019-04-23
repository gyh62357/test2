# -*- coding: utf-8 -*-
# @File  : 1.py
# @Author: 郭迎辉
# @Time  : 2019/3/28/02821:44
# @Desc  :
array_a = [3,2,9,1,6,3,9,5,2,8,4]
array_b = [1,1,5,3,9,0,7,7,6,0,6]
array_c = [5,6,1,7,0,9,4,1,9,4,9]

array_max = []
array_min = []

for i in range(0, len(array_a)):
    array_max.append(max(array_a[i],array_b[i]))
print(array_max)
for i in range(0,len(array_a)):
    array_min.append(min(array_c[i],array_max[i]))
print(array_min)
