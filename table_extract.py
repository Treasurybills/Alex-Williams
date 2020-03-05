# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 23:13:05 2020

@author: econo
"""

import pandas as pd
from pandas_datareader import data as web
import datetime as dt
import numpy as np




#created a function for RSI indicator
def RSI(series, period):
    delta = series.diff().dropna()
    u = delta * 0
    d = u.copy()
    pos_diff = delta > 0
    neg_diff = delta < 0
    u[pos_diff] = delta[pos_diff]
    d[neg_diff] = -delta[neg_diff]
    # first value is sum of avg gains
    u[u.index[period-1]] = np.mean(u[:period])
    u = u.drop(u.index[:(period-1)])
    # first value is sum of avg losses
    d[d.index[period-1]] = np.mean(d[:period])
    d = d.drop(d.index[:(period-1)])
    rs = pd.Series.ewm(u, com=period-1, adjust=False).mean() / \
        pd.Series.ewm(d, com=period-1, adjust=False).mean()
    return 100 - 100 / (1 + rs)

#the stock ticker
stock = 'TSLA'

#start and end data of period under observation
#stipulating the start date
startdate =dt.datetime(2019,1,1)
now = dt.datetime.now()


#extracting stock data from Yahoo Finance
data = web.get_data_yahoo(stock,startdate,now)

# this number is defualt based on calculations I have seen
#we can decide if we want to change this number to match the SMA period, which is currently at 20
period =14
series = data['Adj Close']


#moving average period
ma =10
smastring ='SMA_'+str(ma)

#inserting the SMA and RSI column in the dataframe
data[smastring] = round(data.iloc[:,5].rolling(window = ma).mean(),2)
data['RSI Indicator'] = RSI(series,period)
df = data.rename(columns= {'Close': 'Price'}, inplace =True)
print(data[['Price','SMA_10','RSI Indicator']])

diff = data.Price - data.Price.shift()

data['difference'] = round(diff,2)
print(data.Price, data)

for i in data.index:
    if data['difference'][i] <0:
        print('buy')
    else:
        print(round(data['Price'][i],2))

print(data.iloc[9:][['Price','SMA_10']])

data[['SMA_10','Price']].plot()

