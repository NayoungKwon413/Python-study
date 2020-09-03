'''
Created on 2020. 8. 13.

@author: GDJ24
0813/csvex1.py : csv 파일 읽기
                command 라인에서 입력 파일을 입력받기
'''

import sys
# argv[0] 은 이름
# java 는 파라미터 값부터 0번으로 시작
# python 은 내 프로그래밍 이름부터 0번으로 시작(c언어도 마찬가지)
print(sys.argv[0], sys.argv[1], sys.argv[2])
infile = sys.argv[1]   # cctv3.csv
outfile = sys.argv[2]  # cctv2.csv
with open(infile, "r", newline="") as filereader :
    with open(outfile, "w", newline="") as filewriter :
        header = filereader.readline()
        print(type(header))
        # headlist 의 자료형 : list
        headlist = header.split(",")
        filewriter.write(",".join(map(str, headlist)) + "\r\n")
        for rowlist in filereader :
            filewriter.write(rowlist)