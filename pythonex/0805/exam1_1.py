'''
Created on 2020. 8. 5.

@author: GDJ24
exam1_1.py : 금액을 입력받아서 동전으로 바꿔주는 프로그램 작성하기
    동전의 종류는 500,100,50,10,5,1 의 종류가 있다. 
    입력받은 금액을 동전으로 바꿔줄 때 동전의 갯수는 최소개로 한다. 
'''

money = int(input("교환 받을 금액 : "))
print("필요한 500원 동전 갯수 : ", money//500, "개")
print("필요한 100원 동전 갯수 : ", (money%500//100), "개")
print("필요한 50원 동전 갯수 : ", (money%100//50), "개")
print("필요한 10원 동전 갯수 : ", (money%50//10), "개")
print("필요한 5원 동전 갯수 : ", (money%10//5), "개")
print("필요한 1원 동전 갯수 : ", (money%5), "개")