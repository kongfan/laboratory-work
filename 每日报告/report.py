# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 11:40:59 2018

@author: Administrator
"""

import pandas as pd
#import numpy as np
import datetime
#from pylab import mpl
#mpl.rcParams['font.sans-serif'] = ['Microsoft YaHei']

xlsname = str(datetime.date.today()) + ".xls"

df = pd.read_excel(xlsname)
df.set_index(["住院日期"],inplace = True,drop=False) #设置日期为dataframe的index
df = df[df["状态"] == "在院"]
total = df['住院号'].count() 

section3 = df[df['科室'] == '三病区']['科室'].count()
section4 = df[df['科室'] == '四病区']['科室'].count()
section5 = df[df['科室'] == '五病区']['科室'].count()
section6 = df[df['科室'] == '五病区']['科室'].count()
section7 = df[df['科室'] == '疗养病区']['科室'].count()
section9 = df[df['科室'] == '心理病区']['科室'].count()

report = "<note> \n**"+str(datetime.date.today()) + "** 在院总人数为" + str(total) +"人。其中: \n**三病区**在院" + str(section3)+"人，\n"+"**四病区**在院"+ str(section4)+"人，\n"+"**五病区**在院"+ str(section5)+"人，\n"+"**六病区**在院"+ str(section6)+"人，\n"+"**疗养病区**在院"+ str(section7)+"人，\n"+"**心理病区**在院"+ str(section9)+"人。\n</note> \n\n"

with open('C:\\Bitnami\\wordpress-4.9.1-0\\apache2\\htdocs\\wiki\\data\\pages\\report.txt', 'a',encoding='utf8') as f:
    f.write(report)

with open('report.txt', 'a',encoding='utf8') as f:
    f.write(report)
