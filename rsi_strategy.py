# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 20:10:56 2020

@author: econo
"""

import backtrader as bt
import backtrader.feeds as btfeeds
import datetime

class BuySell(bt.observers.BuySell):
    plotlines = dict(
            buy = dict(marker = '^', markersize = 8.0, color = 'blue', fillstyle = 'full'),
            sell = dict(marker = 'v', markersize = 8.0, color = 'red', fillstyle = 'full'))

class BackTest(bt.Strategy):
    
    def log(self, txt):
        dt = self.datas[0].datetime.date(0).isoformat()
        print(f'{dt}, {txt}')
    
    def notify_order(self,order):
        if order.status in [order.Submitted or order.Accepted]:
            #If an order was submitted/accepted to/by a broker, do nothing
            return
        if order.status in [order.Completed]: 
            #if the order was completed make a log of the type of transaction
            
            if order.isbuy():
                self.log('Buy Executed, %.2f' % order.executed.price)
            elif order.issell():
                self.log('Sell Executed, %.2f' % order.executed.price)
            self.bar_executed = len(self)
        
    def __init__(self):
        self.data_close =self.datas[0].close
        self.order = None
        self.bar_executed = len(self)
        self.sma = bt.indicators.SimpleMovingAverage(self.datas[0], period=20)
        self.rsi = bt.indicators.RelativeStrengthIndex()


        
    def next(self):
        self.log(f'Close, {self.data_close[0]:.2f}')
        self.getposition()
        if not self.position:
            if (self.rsi[0] < 30):
                self.log(f'Buy created at {self.data_close[0]:.2f}')
                self.order = self.buy()

        else:
            if (self.rsi[0] > 70):
                self.log(f'Sell created at {self.data_close[0]:.2f}')
                self.order = self.sell()
        
        #if self.data_close[0] < self.data_close[-1]:
            #if self.data_close[-1] < self.data_close[-2]:
                #self.log(f'Buy now at: {self.data_close[0]:.2f}')
                #self.order = self.buy()
               # self.order = None
       # else:
           # if len(self) >= (self.bar_executed + 15):
                # Sell every 15 days, portfolio final value varies with the days we use
                #could use a widget to find the optimal day to sell
                        #self.log('Sell Create, %.2f' %self.data_close[0] )
                        #self.order = self.sell()

      
       
                
cerebro = bt.Cerebro(stdstats = False)

# I downloaded and pasrsed TSLA data from Yahoo Finance 
#and converted it into a feed for backtrader
data = btfeeds.YahooFinanceData(
    dataname='AAPL',
    #start date
    fromdate=datetime.datetime(2019, 2, 11),
    #end date
    todate=datetime.datetime(2020, 2, 10),
    #all null values are assigned zeros
    nullvalue=0.0,
    # formatting of the date
    dtformat=('%Y-%m-%d'),

    datetime=0,
    high=2,
    low=3,
    open=1,
    close=4,
    volume=5,
    #open interest is not in the csv file so we use -1 to say it's not there
    openinterest=-1
)

size =(16,8)
#setting initial investment
cerebro.broker.set_cash(100000)

# adding the data to cerebro
cerebro.adddata(data)
cerebro.addstrategy(BackTest)
cerebro.addobserver(BuySell)
cerebro.addobserver(bt.observers.Value)
cerebro.addsizer(bt.sizers.FixedSize, stake = 50) #size of the amount of shares to buy/sell

print(f'Starting Portfolio Value: {cerebro.broker.getvalue():.2f}')
cerebro.run()
print(f'Final Portfolio Value: {cerebro.broker.getvalue():.2f}')

# plot results
cerebro.plot(iplot = False , volume = True)
                
        
            