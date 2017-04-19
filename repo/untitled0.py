# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 15:19:08 2017

@author: Administrator
"""

import pandas as pd


list = ["f.xls", "k.xls", "l.xls", "q.xls", "x.xls"]
df = ["f","k","l","q","x"]


for i in list:

#    xls = pd.read_excel(1,sheetname=0,skiprows=6,skip_footer=0)
#    xls.to_excel('total.xls', sheet_name='Sheet1', engine="io.excel")
#    print xls
    
    
    xls = pd.read_excel(i, sheetname=0, skiprows=6, skip_footer=0)
    xls
    xls.to_excel('total.xls', sheet_name='Sheet1')