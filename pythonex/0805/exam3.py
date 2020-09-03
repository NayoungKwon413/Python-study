'''
Created on 2020. 8. 5.

@author: GDJ24
exam3.py : 숫자를 입력받아 입력된 값까지의 전체 합, 짝수합, 홀수합을 구하기
'''

maxnum = int(input("숫자를 입력하세요 : "))
sum = 0
for i in range(1, maxnum+1) :
    sum += i
print(maxnum, "까지의 전체합 : ", sum)

sum = 0
for i in range(0, maxnum+1, 2) :
    sum += i
print(maxnum, "까지의 짝수합 : ", sum)

sum = 0
for i in range(1, maxnum+1, 2) :
    sum += i
print(maxnum, "까지의 홀수합 : ", sum)