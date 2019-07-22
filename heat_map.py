from pandas_datareader import data as pdr
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import yfinance as yf

bitcoin = pdr.get_data_yahoo(['BTC-USD'], '06/01/14')['Close']
sixty = pdr.get_data_yahoo('VBINX', '06/01/14')['Close']
comm = pdr.get_data_yahoo(['COMT'], '06/01/14')['Close']
stocks = pdr.get_data_yahoo(['^GSPC'], '06/01/14')['Close']
real_estate = pdr.get_data_yahoo(['ARE'], '06/01/14')['Close']
bonds = pdr.get_data_yahoo(['BOND'], '06/01/14')['Close']

#print(bitcoin.head())



#df = pd.DataFrame(close_all)
#sf = pd.DataFrame(close_sixty)

result = pd.merge(bitcoin, sixty, on='Date')
result_one = pd.merge(result, comm, on='Date')
result_two = pd.merge(result_one, stocks, on='Date')
result_three = pd.merge(result_two, real_estate, on='Date')
result_four = pd.merge(result_three, bonds, on='Date')
xx = pd.DataFrame(result_four)
#print(xx.head())
xx.set_axis(['Bitcoin', '60/40', 'Commodities', 'Stocks', 'Real Estate', 'Bonds'], axis=1, inplace=True)
print(xx.head())
returns = xx.pct_change()
#You'll probably have to just do everything manually unfortunately
#all['Close'].fillna(method='bfill', inplace=True)
#sf = all['Close'].drop_duplicates(keep=False,inplace=True)

#df = pd.DataFrame(sf)
returns_means = returns.rolling(1).mean()
correlation = returns_means.corr()
print(correlation)
sns.set(style="white")
f, ax = plt.subplots(figsize=(6, 6))
#cmap = sns.diverging_palette(220, 10, as_cmap=True)


mask = np.zeros_like(correlation, dtype=np.bool)
mask[np.triu_indices_from(mask, k=1)] = True
bx = sns.heatmap(correlation, mask=mask, fmt='.2f', annot=True, linewidths=.5, cmap="Blues", robust=True)

for text in bx:
    print(text)


plt.show(bx)
