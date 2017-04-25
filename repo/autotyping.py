# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 14:48:50 2017

@author: kongfan

将汉字字符串变为首字母缩写字符串,快捷方式 win+G  #g::

"""

import csv
import os



with open('2.csv','r') as csvfile:
    reader = csv.DictReader(csvfile)
    ckl = [row['ckl'] for row in reader]       # 每种药品出库的数量

with open('2.csv','r') as csvfile:
    reader = csv.DictReader(csvfile)
    bma = [row['bma'] for row in reader]       # 需要损益的药品的名称拼音编码

len = len(bma)

with open('2.ahk', 'w') as f:                  # 通过python脚本编写ahk脚本，生成的文件名为2.ahk
    f.write("#g::\n")

    for i in range(len):
        f.write("send "+str(bma[i])+"\n")
        f.write("sleep 2000"+"\n")
        f.write("send {enter}"+str(ckl[i])+"{enter}"+"\n")


print "caution : please make sure that the input status is English "
print "please click the close button to exit this window and press win+G to start autotyping !"

os.system("2.ahk") 				# 系统自动运行ahk脚本 ,最小化到托盘区域
