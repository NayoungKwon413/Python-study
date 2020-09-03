'''
Created on 2020. 8. 10.

@author: GDJ24
0810/functionex3.py : 1. 리턴값을 두개이상 반환 => 리스트로 반환
                 2. 가변매개변수 함수
'''

def multi(v1, v2):
    list = []
    res1 = v1 + v2
    res2 = v1 - v2
    list.append(res1)
    list.append(res2)
    return list

def multiParam(* p):   # * p : 매개변수 p 는 가변매개변수. 매개변수 갯수 상관없이 0개 이상 들어올 수 있음
    result = 0
    for i in p:
        result += i
    return result

list = []
hap,sub = 0,0
list = multi(100,200)
hap = list[0]
sub = list[1]
print("multi 함수의 리턴 : %d, %d " % (hap, sub))

print("multiParam() = ", multiParam())
print("multiParam(10) = ", multiParam(10))
print("multiParam(10,20) = ", multiParam(10,20))
print("multiParam(10,20,30) = ", multiParam(10,20,30))

#list = []
hap,sub = 0,0
list = multi(100,200)   # 전역변수 선언 주석처리 해도 list=multi(100,200) 을 통해 list로 삽입
hap = list[0]
sub = list[1]
print("multi 함수의 리턴 : %d, %d " % (hap, sub))

#list = []
hap,sub = 0,0
#list = multi(100,200)
multi(100,200)    # 전역변수 list 선언 없어도 multi 함수 안에 있는 리스트에 선언됨
hap = list[0]
sub = list[1]
print("multi 함수의 리턴 : %d, %d " % (hap, sub))