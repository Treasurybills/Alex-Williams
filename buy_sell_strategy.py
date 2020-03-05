# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 12:55:25 2020

@author: econo
"""
import backtrader as bt
import backtrader.feeds as btfeeds
import datetime

class BuySell(bt.observers.BuySell):
    plotlines = dict(
            buy = dict(marker = '^', markersize = 8.0, color = 'blue', fillstyle = 'full'),
            sell = dict( marker = 'v', markersize = 8.0, color = 'red', fillstyle = 'full'))
    

class TestStrategy(bt.Strategy):

    def log(self, txt):
        #Logging our trade by date [0] means the current day
        dt = self.datas[0].datetime.date(0).isoformat()
        print(f'{dt},{txt}')

    def __init__(self):
        # Keep a reference to the "close" line in the data[0] dataseries
        self.dataclose = self.datas[0].close
        #keeping track of our order status
        self.order = None
    
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
        #if the order was cancelled make a log
        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
            self.log('Order Canceled/Margin/Rejected')

        # Write down: no pending order and the process starts over again
        self.order = None
                    

    def next(self):
        # Simply log the closing price of the series from the reference
        self.log('Close, %.2f' % self.dataclose[0])
        
        
        if self.dataclose[0] < self.dataclose[-1]:
            # current day close is less than previous day close

            if self.dataclose[-1] < self.dataclose[-2]:
                # prior day is less than the day before the prior day
                

                # Buy when there's two consecutive days of a dip
                    self.log('Buy Create, %.2f' % self.dataclose[0])
                    self.order = self.buy()
        else:
            if len(self) >= (self.bar_executed + 15):
                # Sell every 15 days, portfolio final value varies with the days we use
                #could use a widget to find the optimal day to sell
                        self.log('Sell Create, %.2f' %self.dataclose[0] )
                        self.order = self.sell()

#Cerebro is seen as the link between the strategy and the feed
cerebro = bt.Cerebro(stdstats = False)

# I downloaded and pasrsed TSLA data from Yahoo Finance 
#and converted it into a feed for backtrader
data = btfeeds.YahooFinanceData(
    dataname='TSLA',
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
cerebro.addstrategy(TestStrategy)
cerebro.addobserver(BuySell)
cerebro.addobserver(bt.observers.Value)
cerebro.addsizer(bt.sizers.FixedSize, stake = 50) #size of the amount of shares to buy/sell

print(f'Starting Portfolio Value: {cerebro.broker.getvalue():.2f}')
cerebro.run()
print(f'Final Portfolio Value: {cerebro.broker.getvalue():.2f}')

# plot results
cerebro.plot(iplot=True, volume=False, figsize = size)
