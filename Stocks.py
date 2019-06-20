import pandas as pd

df = pd.read_csv('Workbook.csv')
df_corr = df.corr()
print(df_corr)
