'''
Created on 2020. 8. 18.

@author: GDJ24
0818/excelex2.py : xlsx의 모든 sheet 읽기
'''

import openpyxl

filename = "sales_2015.xlsx"
book = openpyxl.load_workbook(filename)
# book.worksheets : sheet 의 리스트
for sheet in book.worksheets :
    data = []
    # sheet.rows : sheet 의 행들
    # row : 한 줄
    # i : index 값, c : 값
    for row in sheet.rows :
        line = []
        for i, c in enumerate(row) :
            line.append(c.value)
        print(line)
        data.append(line)
print(data)