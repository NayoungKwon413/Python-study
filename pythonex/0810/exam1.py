'''
Created on 2020. 8. 10.

@author: GDJ24
0810/exam1.py : 피보나치 수열 출력하기

'''

def fibo(num):
    list = []
    num1 = 0
    num2 = 1
    num3 = num1 + num2
    list.append(num1)
    list.append(num2)
    list.append(num3)
    for i in range(3, num):
        num1 = num2
        num2 = num3
        num3 = num1 + num2
        list.append(num3)
    return list

num = int(input("피보나치 수열의 요소 갯수를 입력하세요(3이상의 값) : "))
print("f(", num, ")=", end="")
print(fibo(num))
