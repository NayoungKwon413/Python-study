'''
Created on 2020. 8. 19.

@author: GDJ24
0819/excelex8.py : 폴더에 속한 excel 파일을 선택
'''
import pandas as pd
import glob  # 경로명 표현시 
import os  # 시스템 관련된 모듈. 

inpath = "D:/20200703back/20200522back/20200522back/python/workspace/pythonex/excel"
outfile = "sales_all.xlsx"
# "*.xlsx" : inpath 폴더 안에 모든 xlsx 파일을 선택
# "*.xls*" : inpath 폴더 안에 모든 xls 파일을 선택
excels = glob.glob(os.path.join(inpath, "*.xlsx"))  # 모든 엑셀파일들을 분류하여 excels에 저장(list형)
print(type(excels))   # list
rows = []   # DataFrame 객체를 리스트로 저장하는 객체
for excel in excels :
    print(excel)
    dfs = pd.read_excel(excel, sheet_name=None, index_col=None)
    for sheet_name, df in dfs.items() :
        rows.append(df)
# excel 파일로 저장
# axis=0 : row 추가
# df_concat : 지정된 폴더에 있는 엑셀파일의 모든 sheet의 데이터를 저장하고 있음.
#             row 형태로 추가됨.
data_concat = pd.concat(rows, sort=False, axis=0, ignore_index=True)
print(type(data_concat))   # DataFrame
writer = pd.ExcelWriter(outfile)
data_concat.to_excel(writer, sheet_name="all_data_all_worksheet", index=False)
writer.save()