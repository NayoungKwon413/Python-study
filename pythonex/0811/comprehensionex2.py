'''
Created on 2020. 8. 11.

@author: GDJ24
comprehensionex2.py : 컴프리헨션을 이용한 set 
'''

set1 = {x**2 for x in [1,2,3]}
print(set1)

set1 = {x**2 for x in [1,1,2,2,3,3]}   # set 이므로 중복되는 값은 제외됨.
print(set1)

list1 = [x**2 for x in [1,1,2,2,3,3]]  # set과 list 차이 : 중복 허용 유무, 정렬 유무
print(list1)

# 1부터 10까지의 수 중 짝수의 제곱을 출력하기
set2 = {x**2 for x in range(1, 11) if x%2 == 0}
print(set2)
print(sorted(set2))