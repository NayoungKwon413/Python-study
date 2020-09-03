'''
Created on 2020. 8. 6.

@author: GDJ24
exam.py : 삼각형 출력하기
삼각형의 높이를 입력받은 후 삼각형을 출력하는 프로그램 작성하기
삼각형의 높이를 입력하세요 : 3
*
**
***
'''

num = int(input("삼각형의 높이를 입력하세요 : "))
for i in range(1, num+1) :
    print("*" * i)
print()
for i in range(num, 0, -1) :
    print("*" * i) 
print()
for i in range(1, num+1) :
    print(" " * (num-i), end="")
    print("*" * i)
print()
for i in range(num, 0, -1) :
    print(" " * (num-i), end="")
    print("*" * i)
print()
for i in range(1, num+1) :
    print(" " * (num-i), end="")
    print("*" * (i*2-1))
print()
for i in range(num, 0, -1) :
    print(" " * (num-i), end="")
    print("*" * (i*2-1))