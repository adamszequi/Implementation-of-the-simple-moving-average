# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 19:41:00 2019

@author: Dell
"""


'''

The moving average is basically the price average over a certain time period, with
equal weight being used for each price. The time period over which it is averaged is often
referred to as the lookback period or history.

The formula = summation of prices from period to n/n

This code computes moving average over a 20 day period
'''

import statistics as stats
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

n=20 #where n is the time period as described
historicalValues=[]
SMAvalues=[]

#download data
data=yf.download('GOOG',start='2015-9-1',end='2018-11-11')
adjustedClose=data['Adj Close']

#set parameters for finding meaning of 20 periods
for closePrice in adjustedClose:
    historicalValues.append(closePrice)
    if len(historicalValues)>n:
        del(historicalValues[0])
    SMAvalues.append(stats.mean(historicalValues))

#Create dataframe for variables
closePrice=pd.DataFrame(adjustedClose,index=data.index)
closePrice['20dayMA']=SMAvalues
closePrice['adjustedPrice']=adjustedClose

plotClosePrice=closePrice['adjustedPrice']
plot20dayMA=closePrice['20dayMA']

#visualise code
fig=plt.figure()
axis=fig.add_subplot(111,ylabel='Plot of google stocks moving average')
plotClosePrice.plot(ax=axis, color='g', lw=2., legend=True)
plot20dayMA.plot(ax=axis, color='r', lw=2., legend=True)
plt.show()









    
    


