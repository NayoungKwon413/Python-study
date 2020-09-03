'''
Created on 2020. 8. 20.

@author: GDJ24
0820/numpy3.py : numpy 예제. 배열 사본 생성, 재구조화 예제
'''

import numpy as np
# 0부터 9까지 임의의 난수 10개를 배열로 저장
x = np.random.randint(10, size=10)  
x_sub = x[:2]   # 0부터 1번 인덱스까지 부분 배열
print(x)
print(x_sub)
x_sub[0] = 20   # 사본(x_sub)의 0번쨰 요소를 20으로 바꾸면 원본(x)도 바뀜
print(x)
print(x_sub)

# 배열 복사
x_cop = x.copy()
x_cop[0] = 100
print(x)
print(x_cop)

# 배열 재편성
x2 = x.reshape(5,2)  # x: 1차원 배열 =>  x2: 5행 2열의 2차원 배열로 재편성
print(x2)

# 0부터 9까지의 임의의 수를 9개 가지고 있는 배열 a
# a배열을 3행 3열로 배열로 재편성하기
# 재편성시 요소 갯수가 맞아야 함. size=10일때 오류발생
a = np.random.randint(10, size=9)
a2 = a.reshape(3,3)
print(a)
print(a2)