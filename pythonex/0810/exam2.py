'''
Created on 2020. 8. 10.

@author: GDJ24
0810/exam2.py : 문자열 문제
'''

ss = "홍길동"  
# 홍#길#동#  으로 출력하기
print(ss[0],end="#")
print(ss[1],end="#")
print(ss[2],end="#")
print()

for i in range(len(ss)):
    print(ss[i],end="#")
print()

# 동길홍 으로 출력하기
for i in range(len(ss)-1, -1, -1):
    print(ss[i], end="")
print()

print(ss[::-1])