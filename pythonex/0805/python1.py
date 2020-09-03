'''
Created on 2020. 8. 5.

@author: GDJ24
python1.py : 파이썬 예제1

    1. ''' ''' 여러줄 주석
       #        한줄 주석
    2. 변수 선언 필요 없음 : 자료형은 있으나, 선언 필요없이 처음 들어오는 자료의 자료형을 인식. 자동 변환도 가능
    3. {  } 중괄호 블럭이 없음
            공백으로 처리

'''
#한줄 주석
print("Hello World")

sel = int(input('입력 진수 결정(16/10/8/2) : '))
num = input("값 입력 : ")
if sel == 16 : 
    # int() 형변환 연산자
    # num, 16 : 문자열 num을 16진수로 인식하여 정수형으로 리턴
    num10 = int(num, 16)   # 앞에 공백으로 {  } 블럭 처리
    print("16진수 ", num, " : ", num10)
if sel == 10 : 
    num10 = int(num, 10)  
    print("10진수 ", num, " : ", num10)
if sel == 8 : 
    num10 = int(num, 8)  
    print("8진수 ", num, " : ", num10)
if sel == 2 : 
    num10 = int(num, 2)
    print("2진수 ", num, " : ", num10)
print(num10)
print(type(num))
num = num10
print(type(num))
#10진수를 16, 8, 2 진수로 변경하여 출력하기
print("16진수 => ", hex(num10))
print("8진수 => ", oct(num10))
print("2진수 => ", bin(num10))