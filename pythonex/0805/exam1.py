'''
Created on 2020. 8. 5.

@author: GDJ24
exam1.py : 금액을 입력받아서 동전으로 바꿔주는 프로그램 작성하기
    동전의 종류는 500,100,50,10,5,1 의 종류가 있다. 
    입력받은 금액을 동전으로 바꿔줄 때 동전의 갯수는 최소개로 한다. 
'''

num = int(input("금액을 입력해주세요 : "))
print("500원 : ", (num // 500), "개") 
num = num-500*(num//500)
print("100원 : ", (num // 100), "개") 
num = num-100*(num // 100)
print("50원 : ", (num // 50), "개") 
num = num-50*(num // 50)
print("10원 : ", (num // 10), "개") 
num = num-10*(num // 10)
print("5원 : ", (num // 5), "개") 
num = num-5*(num // 5)
print("1원 : ", (num // 1), "개") 
