# -*- coding: utf -8 -*-

"""
Author : kongfan@outlook.com
create : 2017-4-7

"""


import requests
import time


retracement = 0.001                   # 浮点数 ,从极值位回撤
ticker = "sz162411"                   # ticker字符型，证券代码，如："sz150312"

"""

    函数 getTickRTSnapshot(ticker):

    ticker字符型，证券代码，如："sz150312"

    获取证券代码为ticker的证券实时行情

"""
def getTickRTSnapshot(ticker):

    resp = requests.get("http://hq.sinajs.cn/list="+ticker)
    res = resp.text.split(",")
    snapshot = dict()
    snapshot['shortNM'] = res[0][-4:]              # 证劵简称
    snapshot['openPrice'] = float(res[1])          # 今日开盘价
    snapshot['prevClosePrice'] = float(res[2])     # 昨收盘价格
    snapshot['lastPrice'] = float(res[3])          # 最新价格
    snapshot['highPrice'] = float(res[4])          # 最高价格
    snapshot['lowPrice'] = float(res[5])           # 最低价格
    snapshot['volume'] = float(res[8])             # 成交数量
    snapshot['value'] = float(res[9])              # 成交金额
    snapshot['bidBook_volume1'] = float(res[10])   # 一档买入交易量
    snapshot['bidBook_price1'] = float(res[11])    # 一档买入价格
    snapshot['askBook_volume1'] = float(res[20])   # 一档卖出交易量
    snapshot['askBook_price1'] = float(res[21])    # 一档卖出价格
    snapshot['dataDate'] = res[30]                 # 交易日期(yyyy-MM-dd)
    snapshot['dataTime'] = res[31]                 # 交易时间'HH:mm:ss'
   # snapshot['average'] = snapshot['value'] / snapshot['volume']           # 当日均价
    return snapshot

deviation = 0.01                   # 偏离均线幅度
retracement = 0.002                # 回撤值大小

print getTickRTSnapshot('sz162411')
average = snapshot['value'] / snapshot['volume']           # 当日均价
print average

#
#                        for i in getTickRTSnapshot('sz162411):
#    print i

#i = 1

#while i < 3:
#    if (lastPrice < average * (1-deviation) and
#       lastPrice > lowPrice + retracement):
#        print(i, shortNM, dataTime,  | 现价: f%  均价: f% | 卖点: f%  买点: f% | 偏幅: f%" %
#            (i, shortNM, dataTime, lastPrice, average, average * (1+deviation),
#             average * (1+deviation), (lastPrice - average) / average))
##print u"d% s% s%   现价: f%  均价: f%  卖点: f%  买点: f%  偏幅: f%" %(i, shortNM, dataTime, lastPrice, average, average * (1+deviation), average * (1-deviation), (lastPrice - average) / average)


# dealTimes = len(user.current_deal)   # 成交次数
