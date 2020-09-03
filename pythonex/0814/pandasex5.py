'''
Created on 2020. 8. 14.

@author: GDJ24
0814/pandasex5.py : column 선택하기
    iloc : 인덱스를 기준으로 조회
    loc  : 이름을 기준으로 조회
'''

import pandas as pd
 
infile="supplier_data.csv"
df = pd.read_csv(infile)
df_col = df.iloc[:, [0,3]]   # [행, 열] => 모든 행, 0번, 3번열 조회
print("df.iloc[:, [0,3]] => ")
print(df_col)
print("행: 0~3개의 행, 열: 0~2개의 열")
df_col = df.iloc[0:4, 0:3]
print(df_col)

# 모든 행의 Invoice Number, Cost 컬럼 조회하기
df_col = df.loc[:, ["Invoice Number", "Cost"]]
print(df_col)

# Invoice Number 값이 920- 로 시작하는 행의 Invoice Number 와 Cost 컬럼 조회하기
df_col = df.loc[df["Invoice Number"].str.startswith("920-"), ["Invoice Number", "Cost"]]
print(df_col)