'''
Created on 2020. 8. 13.

@author: GDJ24
0813/fileex1.py : 파일 읽기
    open("파일이름", "모드", 인코딩방식)
      파일모드
      "r" : 읽기 모드
      "w" : 쓰기 모드
      "r+" : 읽기/쓰기
      "a" : append 약자. 쓰기모드, 기존 파일이 있는 경우 내용이 추가됨.
      "t" : Text 모드. 문자형 (문자열로 읽음). 생략가능. 기본형
      "b" : Binary 모드. 이진형(바이트형)
'''

infp = None
inStr = ""
infp = open("regularex3.py", "rt", encoding='UTF8')
while True : 
    inStr = infp.readline()
    if inStr == None:   # EOF(End of File)
        break
    print(inStr, end="")
infp.close()