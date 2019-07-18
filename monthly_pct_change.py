from pandas_datareader import data as pdr
import pandas as pd
import numpy as np
import yfinance as yf

all = pdr.get_data_yahoo(['BTC-USD', 'DCR-USD', 'ZEC-USD'], '06/01/17')
sixty = pdr.get_data_yahoo('VBINX', '06/01/17')

close_all = all[['Close']]
close_sixty = sixty[['Close']]

df = pd.DataFrame(close_all)
sf = pd.DataFrame(close_sixty)

result = pd.merge(close_sixty, close_all, on='Date')
xx = pd.DataFrame(result)
xx.set_axis(['XBINX', 'BTC', 'DCR', 'ZEC'], axis=1, inplace=True)

returns = xx.pct_change()
#You'll probably have to just do everything manually unfortunately
#all['Close'].fillna(method='bfill', inplace=True)
#sf = all['Close'].drop_duplicates(keep=False,inplace=True)

#df = pd.DataFrame(sf)
returns_means = returns.rolling(30).mean()
correlation = returns_means.corr()

monthly = result.resample('BM', how=lambda x: x[-1])

#print(monthly)

monthly_pct = monthly.pct_change()

print(monthly_pct)

monthly_corr = monthly_pct.corr()

print(monthly_corr)
