# -*- coding: utf-8 -*-

"""


"""


import requests
#import time

#dealTimes = len(user.current_deal)   #成交次数
#ticker = #被交易证券六位数代码 

res = requests.get("http://hq.sinajs.cn/list=sz150312").text.split(",")

# print resp
# res = resp.
   

    
shortNM = res[0][-4:]                #证劵简称
# openPrice = float(res[1],3)          #今日开盘价
# prevClosePrice = float(res[2],3)     #昨收盘价格  
# lastPrice = float(res[3],3)          #最新价格
# highPrice = float(res[4],3)          #最高价格
# lowPrice = float(res[5],3)           #最低价格
# volume = float(res[8],3)             #成交数量
# value = float(res[9],3)              #成交金额
# bidBook_volume1 = float(res[10],3)   #一档买入交易量
# bidBook_price1 = float(res[11],3)    #一档买入价格
# askBook_volume1 = float(res[20],3)   #一档卖出交易量
# askBook_price1 = float(res[21],3)    #一档卖出价格
# dataDate = res[30]                   #交易日期(yyyy-MM-dd)
# dataTime = res[31]                   #交易时间'HH:mm:ss'


print shortNM

