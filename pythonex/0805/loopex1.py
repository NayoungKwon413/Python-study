'''
Created on 2020. 8. 5.

@author: GDJ24
loopex1.py : 반복문 연습
'''

num = 0
while num < 5 :
    print(num, end=",")
    num += 1
    
print("\nfor 구문")
# range(0,5) : 0,1,2,3,4 0부터 4까지의 값들을 의미
for i in range(0,5) :
    print(i,end=",")
    
#1부터 100까지의 합 구하기
sum = 0;
for i in range(1, 101) :
    sum += i
print("\n1부터 100까지의 합 : ", sum)

#1부터 100까지의 짝수의 합 구하기
sum = 0
for i in range(1, 101) :
    if(i % 2 == 0) :
        sum += i
        
print("\n1부터 100까지의 짝수의 합 : ", sum)

sum = 0
for i in range(0, 101, 2) :
        sum += i
        
print("\n1부터 100까지의 짝수의 합 : ", sum)

sum = 0
for i in range(1, 101, 2) :
        sum += i
        
print("\n1부터 100까지의 홀수의 합 : ", sum)