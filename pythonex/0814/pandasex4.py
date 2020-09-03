'''
Created on 2020. 8. 14.

@author: GDJ24
0814/pandasex4.py : pandas 부분 선택 예제 
'''

import pandas as pd

infile = "supplier_data.csv"
outfile = "pandas_out4.csv"

df = pd.read_csv(infile)
print(df)
print("===============")
print(df["Invoice Number"].str.startswith("920-"))
print("===============")
df_inset = df.loc[df["Invoice Number"].str.startswith("920-")]
print(df_inset)
df_inset.to_csv(outfile, index=False)
