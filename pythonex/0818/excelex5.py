'''
Created on 2020. 8. 18.

@author: GDJ24
0818/excelex5.py : pandas 를 이용하여 excel 파일 읽고 쓰기
'''

import pandas as pd

infile = "sales_2015.xlsx"
outfile = "sales_2015_pd.xlsx"
# read_excel(file이름, sheet 이름, index여부)
df = pd.read_excel(infile,"january_2015", index_col=None)
print(df)
# df에 조건 : Sale Amount 값이 500 보다 큰 값만 outfile에 저장하기
df_value = df[df["Sale Amount"].astype(float) > 500.0]  # df 중에 Sale Amount가 500보다 큰 값만 df_value에 저장
# ExcelWriter(출력파일이름, xls 기본)
# engine="openpyxl" : xlsx 파일로 출력
writer = pd.ExcelWriter(outfile, engine="openpyxl")
# to_excel : DataFrame 데이터를 excel 파일로 변환
df_value.to_excel(writer, sheet_name="jan_15_out", index=False)
writer.save()

