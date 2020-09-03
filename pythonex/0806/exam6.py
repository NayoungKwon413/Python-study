'''
Created on 2020. 8. 6.

@author: GDJ24
exam.py : 리스트 문제
    aa, bb 배열을 생성하고,
    aa 배열은 0부터 짝수 20개를 저장
    bb 배열은 aa 배열의 역순으로 값을 저장
    aa, bb 배열의 값을 출력하기
'''


aa, bb = [],[]
value = 0
for i in range(0, 20) :
    aa.append(value)
    value += 2
for i in range(0, len(aa)) :
    bb.append(aa[len(aa)-1-i])
#for i in range(-1, -21, -1) :
#    bb.append(aa[i])
print(aa)
print(bb)