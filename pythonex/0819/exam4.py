'''
Created on 2020. 8. 19.

@author: GDJ24
0819/exam4.py : 컬럼만 선택하기
                sales_2013.xlsx 파일의 모든 sheet 의 열이 'Customer Name', 'Sale Amount' 컬럼만
                sales_2013_allamt.xlsx 파일로 저장하기
'''

import pandas as pd

infile = "sales_2013.xlsx"
outfile = "sales_2013_allamt.xlsx"
writer = pd.ExcelWriter(outfile)
col_name = ['Customer Name', 'Sale Amount']
df = pd.read_excel(infile, sheet_name=None, index_col=None)
for worksheet_name, data in df.items() :
    print("===", worksheet_name, "===")
    data_value = data.loc[:,col_name]
    data_value.to_excel(writer, sheet_name=worksheet_name, index=False)
writer.save()