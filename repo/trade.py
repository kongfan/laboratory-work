# -*- coding: utf-8 -*-
"""

This is a python script for trade.


"""

import time
#import easytrader
import tushare as ts

try:
    #user = easytrader.use('yh', debug=False)
    #user.prepare('yh.json')
except:
    print u"登录失败!"

buy_times = 0
sell_times = 0

symbols = u'150312'       # 被交易证券六位数代码

deviation = 0.009         # 偏离均价线的幅度
retracement = 0.001       # 从高位回撤的值

i = 1
while True:
    try:
        snap = ts.get_realtime_quotes(symbols)

        average = float(snap.amount[0])/float(snap.volume[0])   # 当日实时均价
        unit_amount = int(1500/float(snap.price[0])/100)*100    # 单次买卖的数量
        shortNM = snap.name[0]                                  # 证劵简称
        openPrice = float(snap.name[0])                         # 今日开盘价
        prevClosePrice = float(snap.name[0])                    # 昨收盘价格
        lastPrice = float(snap.price[0])                        # 最新价格
        highPrice = float(snap.high[0])                         # 最高价格
        lowPrice = float(snap.low[0])                           # 最低价格
        volume = float(snap.volume[0])                          # 成交数量
        value = float(snap.amount[0])                           # 成交金额
        bidBook_volume1 = float(snap.b1_v[0])                   # 一档买入交易量
        bidBook_price1 = float(snap.b1_p[0])                    # 一档买入价格
        askBook_volume1 = float(snap.a1_v[0])                   # 一档卖出交易量
        askBook_price1 = float(snap.a1_p[0])                    # 一档卖出价格
        dataDate = float(snap.date[0])                          # 交易时间
        dataTime = float(snap.time[0])                          # 交易时间'HH:mm:ss'
        average = round(value / volume, 3)                      # 当日均价
        amplitude = round((lastPrice - average) / average, 5)*100  # 实时振幅
    except:
        print u"获取行情错误!"

    if (lastPrice < average*(1-deviation) and
            lastPrice > lowPrice + retracement):

        print(i, u" | 时间:", dataTime, u" | 现价:", lastPrice, u" | 均价:",
              average, u" | 卖点:", average*(1+deviation), u" | 买点:",
              average*(1-deviation), u" | 偏幅:", amplitude)

        if buy_times < 1:
            #user.buy(symbols, price=bidBook_price1 + 0.001,
            #         amount=unit_amount)

            buy_times = buy_times + 1

            with open('deal.csv', 'a') as f:
                f.write(dataDate, dataTime, 'buy', symbols, unit_amount,
                        (bidBook_price1 + 0.001), '\n')
            print "buy at :", (bidBook_price1 + 0.001), "total :", buy_times

    elif (lastPrice > average * (1 + deviation) and
          lastPrice < highPrice - retracement):

        print(
            i, u" | 时间:", dataTime, u" | 现价:", lastPrice, u" | 均价:",
            average, u" | 卖点:", average*(1+deviation), u" | 买点:",
            average*(1-deviation), u" | 偏幅:", amplitude
        )

        if sell_times < 1:
            #user.sell(symbols, price=askBook_price1 - 0.001,
            #          amount=unit_amount)

            sell_times = sell_times + 1
            with open('deal.csv', 'a') as f:
                f.write(dataDate, dataTime, 'sell', symbols, unit_amount,
                        (askBook_price1 - 0.001), '\n')
            print "sell at :", (askBook_price1 - 0.001), "total :", sell_times

    else:
        print(i, u" | 时间:", dataTime, u" | 现价:", lastPrice, u" | 均价:",
              average, u" | 卖点:", average*(1+deviation), u" | 买点:",
              average*(1-deviation), u" | 偏幅:", amplitude)

    i = i+1
    time.sleep(3)

    if time.strftime("%H:%M", time.localtime(time.time())) == "14:56": #and
            #user.position[0][u"current_amount"] >= unit_amount * 2):

        #user.sell(symbols, price=snap.bid[0], amount=unit_amount)
        with open('deal.csv', 'a') as f:
            f.write(dataDate, dataTime, 'sell', symbols, unit_amount,
                    (bidBook_price1 - 0.001), '收盘清仓 \n')
        break

print time.strftime("%Y-%m-%d", time.localtime(time.time()))+"日内交易策略完成！"
time.sleep(120)
