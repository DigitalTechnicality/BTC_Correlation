from pandas_datareader import data as pdr
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import yfinance as yf

pd.set_option('display.expand_frame_repr', False)

bitcoin = pdr.get_data_yahoo(['BTC-USD'], '06/01/14')['Close']
sixty = pdr.get_data_yahoo('VBINX', '06/01/14')['Close']

result = pd.merge(bitcoin, sixty, on='Date')
xx = pd.DataFrame(result)
xx.set_axis(['Bitcoin', '60/40'], axis=1, inplace=True)

for col in xx:
    xx['Norm Return' + ' ' + col] = xx[col]/xx[col].iloc[0]


for col, allocation in zip((xx[['Norm Return Bitcoin', 'Norm Return 60/40']]),[0.05, 0.95]):
    xx['Allocation' + ' ' + col] = xx[col] * allocation

zz = xx.rename(columns={'Allocation Norm Return Bitcoin' : 'Allocation Bitcoin', 'Allocation Norm Return 60/40' : 'Allocation 60/40'})

for col in zz[['Allocation Bitcoin', 'Allocation 60/40']]:
    zz['Position' + ' ' + col] = zz[col] * 10000

all_pos = pd.DataFrame(zz[['Position Allocation Bitcoin', 'Position Allocation 60/40']])

all_pos['Total_Pos'] = zz['Position Allocation Bitcoin'] + zz['Position Allocation 60/40']

cumulative_return = 100 * (all_pos['Total_Pos'][-1]/all_pos['Total_Pos'][0]-1)

#print(cumulative_return)

#print(all_pos.tail(1))

all_pos['Daily_Return'] = all_pos['Total_Pos'].pct_change(1)

annualized_rf = .02/252

Sharpe_Ratio = (all_pos['Daily_Return'].mean())/(all_pos['Daily_Return'].std())

BB = Sharpe_Ratio * np.sqrt(252)

print(BB)


#all_pos['Hmm'] = all_pos.sum(axis=1)

#portf_val = pd.DataFrame

#portf_val.columns = ['Bitcoin Pos', '60/40 Pos']

#portf_val = pd.concat(all_pos, axis=1)

#portf_val['Total_Pos'] = portf_val.sum(axis=1)



#for stock_df, allocation in zip((result), [.05,95]):
    #result['Allocation'] = result['Norm return'] * allocation

#for stock_df in result:
    #stock_df['Position'] = stock_df['Allocation']*10000

#print(all_pos.head())
