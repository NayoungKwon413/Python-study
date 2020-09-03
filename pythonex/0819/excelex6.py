'''
Created on 2020. 8. 19.

@author: GDJ24
0818/excelex6.py : pandas 를 이용하여 xlsx 파일 읽기
    1. xlsx 파일의 모든 sheet 데이터 읽기
    2. 생성되는 excel 파일로 하나의 sheet 로 데이터 저장
       => 조건이 맞는 경우만 저장 가능(필터링)
'''

import pandas as pd

infile = "sales_2015.xlsx"
outfile = "sales_all_2015.xlsx"
df = pd.read_excel(infile, sheet_name=None, index_col=None)
row_output = []   # 모든 sheet 의 데이터 저장
# df.items() : sheet 정보들
#              sheet 이름, sheet 데이터
for worksheet_name, data in df.items() :
    print("===", worksheet_name, "===")
    print(type(data))    # DataFrame
    row_output.append(data[data["Sale Amount"].replace("$",'').replace(",","").astype(float) > 200.0])   # 숫자로 형변환 위해 $와 , 제거 -> 실수형float로 변환 -> 200보다 큰 데이터만 가져옴
# axis=0 : row로 추가
# axis=1 : column으로 추가
filtered_row = pd.concat(row_output, axis=0, ignore_index=True)   # 행으로 데이터 추가
writer = pd.ExcelWriter(outfile, engine="openpyxl")
filtered_row.to_excel(writer, sheet_name="sale_2015", index=False)
writer.save()