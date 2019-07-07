from pandas_datareader import data as pdr
import pandas as pd
import numpy as np
import yfinance as yf


today = '20190621'
yf.pdr_override()
df = pdr.get_data_yahoo('BTC-USD', start='2014-06-20', end='2019-06-20')
sf = pdr.get_data_yahoo('^GSPC', start='2014-06-20', end='2019-06-20')
df.reset_index(inplace=True,drop=False)
sf.reset_index(inplace=True,drop=False)

#for date in df['Date']:
    #for dates in sf['Date']:
        #if(date != dates):
            #df.drop(date)
#print(df)
#print(sf)
#merge = pd.merge(df,sf, how='inner',left_index=True,right_index=True)

result = pd.merge(df,sf,on='Date')

dc = pd.DataFrame(result)

def total_return(prices):
    return prices.iloc[-1] / prices.iloc[0] - 1

dx = dc.set_index('Date').pct_change(periods=30)

#herewego = dx.corr()

herewego = dx.rolling(30).mean()

hmm = herewego.corr()
print(hmm)
