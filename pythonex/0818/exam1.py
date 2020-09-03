'''
Created on 2020. 8. 18.

@author: GDJ24
0818/exam1.py : ssec1804.xls 파일에서 1.남자, 1.여자 sheet 의 내용을 ssec1804mf.xls 파일에 남자, 여자 sheet 로 저장하기
'''

from xlrd import open_workbook
from xlwt import Workbook

def makesheet(output_sheet):   # output_sheet : output_sheet_(fe)male
                               # worksheet : 1.남자(1.여자) sheet 내용
    for row_index in range(worksheet.nrows):  # 선택된 sheet 의 행 선택(sheet가 가지고 있는 행 수만큼)
        for column_index in range(worksheet.ncols):   # 선택된 sheet 의 열 선택
            output_sheet.write(row_index, column_index,worksheet.cell_value(row_index, column_index))
        print(worksheet.cell_value(row_index, column_index))

infile = "ssec1804.xls"
outfile = "ssec1804mf.xls"
worksheet = None   # 전역변수 선언
outworkbook = Workbook()
output_sheet_male = outworkbook.add_sheet("남자")
output_sheet_female = outworkbook.add_sheet("여자")

with open_workbook(infile) as workbook :
    # workbook : ssec1804.xls 파일의 내용
    worksheet = workbook.sheet_by_name("1.남자")
    makesheet(output_sheet_male)
    worksheet = workbook.sheet_by_name("1.여자")
    makesheet(output_sheet_female)
outworkbook.save(outfile)