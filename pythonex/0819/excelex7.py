'''
Created on 2020. 8. 19.

@author: GDJ24
0819/excelex7.py : pandas 를 이용해 xls 파일 읽기
                                 출력되는 excel 파일의 sheet를 여러개로 저장하기
'''

import pandas as pd
infile = "ssec1804.xls"
outfile = "ssec1804_bak.xls"
writer = pd.ExcelWriter(outfile)   # 출력 파일 미리 설정
df = pd.read_excel(infile, sheet_name=None, index_col=None)  # sheet_name=None : 모든 sheet
for worksheet_name, data in df.items() :
    print("===", worksheet_name, "===")
    print(data)
    # data.to_excel : sheet 별로 excel 파일에 저장
    data.to_excel(writer, sheet_name=worksheet_name, index=False, header=False)  # data를 excel파일로 전환
    # sheet_name 설정, header=False: 미설정시 가장 첫 줄 데이터 헤더로 등록됨
writer.save()