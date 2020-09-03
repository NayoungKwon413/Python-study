'''
Created on 2020. 8. 13.

@author: GDJ24
0813/exam1.py : regularex3.py 파일을 읽어서 regularex3.bak 파일로 복사하기
'''

infp, outfp = None, None
inStr = ""
infp = open("regularex3.py", "rt", encoding='UTF8')
outfp = open("regularex3.bak", "w", encoding='UTF8')
while True : 
    inStr=infp.readline()
    if not inStr:
        break
    outfp.writelines(inStr)
infp.close()
outfp.close()
print("프로그램종료")