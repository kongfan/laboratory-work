# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 19:36:01 2017

@author: Administrator
"""

import tushare as ts
import pandas as pd

# pd = ts.get_stock_basics()
# print(pd.head(10))

p = pd.read_excel("2017-4-25.xls")
print p
print(p.head())
