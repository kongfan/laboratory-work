# -*- coding: utf-8 -*-
"""

This is a python script for trade.


"""

import time
import easytrader
import tushare as ts




user = easytrader.use('yh',debug=False) 
#user = easytrader.use('ht',debug=False) 
#user = easytrader.use('ht') 
#user.prepare('ht.json')
user.prepare('yh.json')
buy_times=0
sell_times=0
symbols=u'150312' #被交易证券六位数代码      
#unit_amount=3000  #单次买卖证券的数量（一般是半仓的数量）
ampli=0.009 # 偏离均价线的幅度 
drawdown=0.001 #从高位回撤的值

i = 1
while 1:
    quotations = ts.get_realtime_quotes(symbols) 
    average= float(quotations.amount[0])/float(quotations.volume[0])
    unit_amount=int(1500/float(quotations.price[0])/100)*100  #单次买卖证券的数量（一般是半仓的数量）

    if float(quotations.price[0]) < average*(1-ampli) and float(quotations.price[0]) > (float(quotations.low[0]) + drawdown):
        print str(i)+u"++时间:"+quotations.time[0]+u"  || 现价:"+quotations.price[0]+u"  均价:"+str(round(average,3))\
             +u" |  上限:"+str(round(average*(1+ampli),3))+u"  下限:"+str(round(average*(1-ampli),3))+u" | 偏幅:"+str(round(\
             (float(quotations.price[0])-average)/average,5)*100),"%  "#+"||  仓位 ",user.position[0][u"current_amount"] 

        if buy_times < 1:
            user.buy(symbols, price=float(quotations.price[0])+0.001, amount=unit_amount)
            buy_times=buy_times+1 
            with open('deal.csv', 'a') as f:
                f.write(time.strftime("%Y-%m-%d,%H:%M:%S",time.localtime(time.time()))+',buy,'+symbols+','+str(unit_amount)+','+str(float(quotations.price[0])+0.001)+'\n')
            print "buy at :",str(float(quotations.price[0])+0.001),"total :",buy_times; 
            for a in user.entrust[0]:
                print user.entrust[0][a]#.decode();
        
    elif float(quotations.price[0]) > average*(1+ampli) and float(quotations.price[0]) < (float(quotations.high[0]) - drawdown):
        print str(i)+u"--时间:"+quotations.time[0]+u"  || 现价:"+quotations.price[0]+u"  均价:"+str(round(average,3))\
             +u" |  上限:"+str(round(average*(1+ampli),3))+u"  下限:"+str(round(average*(1-ampli),3))+u" | 偏幅:"+str(round(\
             (float(quotations.price[0])-average)/average,5)*100),"%  "#+"||  仓位 ",user.position[0][u"current_amount"]

        if sell_times < 1:
            user.sell(symbols, price=float(quotations.price[0])-0.001, amount=unit_amount)
            sell_times=sell_times+1 
            with open('deal.csv', 'a') as f:
                f.write(time.strftime("%Y-%m-%d,%H:%M:%S",time.localtime(time.time()))+',sell,'+symbols+','+str(unit_amount)+','+str(float(quotations.price[0])-0.001)+'\n')
            print "sell at :",str(float(quotations.price[0])-0.001),"total :",sell_times;
            print user.entrust #[0][u"entrust_amount"]
            
    else:
        print str(i)+u"**时间:"+quotations.time[0]+u"  || 现价:"+quotations.price[0]+u"  均价:"+str(round(average,3))\
             +u" |  上限:"+str(round(average*(1+ampli),3))+u"  下限:"+str(round(average*(1-ampli),3))+u" | 偏幅:"+str(round(\
             (float(quotations.price[0])-average)/average,5)*100),"%  "#+"||  仓位 ",user.position[0][u"current_amount"]

    i=i+1
    time.sleep(3)
    
    if time.strftime("%H:%M",time.localtime(time.time())) == "14:56" and user.position[0][u"current_amount"] >= unit_amount * 2:
        user.sell(symbols, price=quotations.bid[0], amount=unit_amount)
        with open('deal.csv', 'a') as f:
            f.write(time.strftime("%Y-%m-%d,%H:%M:%S",time.localtime(time.time()))+',sell,'+symbols+','+str(unit_amount)+','+quotations.bid[0]+'\n')
        break

print time.strftime("%Y-%m-%d",time.localtime(time.time()))+"日内交易策略完成！"
time.sleep(120)
