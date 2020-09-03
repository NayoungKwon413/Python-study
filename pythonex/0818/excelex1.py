'''
Created on 2020. 8. 18.

@author: GDJ24
0815/excelex1.py : xlsx 파일 읽기 excel 파일 예제
    xlsx : pip install openpyxl
    xls  : pip install xlrd
'''

import openpyxl # pip install openpyxl 
filename = "sales_2015.xlsx"
book = openpyxl.load_workbook(filename)
sheet = book.worksheets[0]  # 첫번째 sheet
data = []   # 출력을 위해 저장
for row in sheet.rows :
    # row : 한 줄 정보
    line = []
    # d : cell 의 내용
    for l, d in enumerate(row) :
        line.append(d.value)  # 한줄의 셀의 값들을 list 로 저장
#        print(l, end="\t")    # l : cell 의 index 값
    print(line)
    data.append(line)
print(type(data))
print(data)
# enumerate : 리스트에서 데이터와 index 값을 제공
# 해당 데이터가 몇번째 컬럼인지 알 수 있음.
for i, a in enumerate(data) :  # i : index, a : 값
    print(i+1, a)