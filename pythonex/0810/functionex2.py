'''
Created on 2020. 8. 10.

@author: GDJ24
0810/functionex2.py : 전역변수 사용하기
'''

def func1() :
    global gval     # gval 변수는 전역변수로 선언된 변수로 사용함.
    gval = 200      # 전역변수 gval 변수의 값을 변경 
    a = 20    #지역변수
    b = 1000  #지역변수
    print("func1() 함수 호출함", gval, a, b)

def func2() :
    b = 2000
    print("func2() 함수 호출함", gval, a, b)   # 100 10 2000
    func1()                                 # 200 20 1000
    print("전역변수 gval 값=", gval, a, b)     # 100 10 2000

gval = 100   #전역변수 => 모든 함수에서 사용이 가능한 변수
a = 10       #전역변수
if __name__ == '__main__' : #프로그램의 시작. 
    a = 30    #전역변수 => main 함수 안에 존재
    func2()   #함수 호출
    print("__main__ 함수 호출함", gval, a)   # b 출력 시 에러 발생 -> func1() 안에서만 사용가능
    # 200 30 