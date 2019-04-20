# -*- coding: utf-8 -*-
# @File  : test2.py
# @Author: 郭迎辉
# @Time  : 2019/4/16/01616:58
# @Desc  :
import sys
import csv
input_file = ('E://1.csv')
output_file = ('E://1.csv')
header_lise = []
with open(input_file,'r',newline='') as csv_in_file:
    with open(output_file,'w',newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        header_lise = ['']
        for i in range(1,20):
            header_list.append[i]
            filewriter.writerow(header_list)
            for row in filereader:
                filewriter.writerow(row)



