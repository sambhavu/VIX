import yfinance as yf
import yahoofinancials
import numexpr as ne
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


tickersymbol = '^VIX'

VIX = yf.Ticker(tickersymbol)
VIX_df = VIX.history(period = '5y', interval = '1d')
VIX_close = VIX_df['Close'].values
VIX_open = VIX_df['Open'].values
VIX_high = VIX_df['High'].values
VIX_low = VIX_df['Low'].values
VIX_volume = VIX_df['Volume'].values



VIX_t = ['2020-06-23', '2020-06-30', '2020-07-07', '2020-07-14', '2020-07-21', '2020-08-18', '2020-09-15', '2020-10-20', '2020-11-17', '2020-12-15']

for i in range(2):

    VIXCall = VIX.option_chain(VIX_t[i]).calls

    VIXCall_strike = VIXCall['strike']
    VIXCall_iv =  VIXCall['impliedVolatility']
    VIXCall_pc = VIXCall['percentChange']
    #plt.plot(VIXCall_strike, VIXCall_iv)


#plt.show()

ma=0
ma5 = []
vix_iv = []

size = VIXCall_iv.size

for i in range(5,size):
    for j in range(i-5, i):
        ma += VIXCall_iv[j]
    ma = ma/5.0
    ma5.append(ma)


iv_avg = [None,None]

for i in range(2,size):
    iv_average = 0
    change = VIXCall_iv[i] - VIXCall_iv[i-1]
    change2 = VIXCall_iv[i-1] - VIXCall_iv[i-2]

    if(change > 0 and change2 < 0):
        iv_average = (VIXCall_iv[i] + VIXCall_iv[i-1])/2.0
    if(change < 0 and change2 > 0):
        iv_average = (VIXCall_iv[i] + VIXCall_iv[i-1])/2.0

    if iv_average == 0:
        iv_avg.append(VIXCall_iv[i])
    else:
        iv_avg.append(iv_average)



plt.plot(VIXCall_iv)
plt.plot(iv_avg)
#plt.plot(ma5)
plt.show()





