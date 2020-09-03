'''
Created on 2020. 8. 20.

@author: GDJ24
0820/numpy2.py : numpy 예제. 기능 실습
'''

import numpy as np

x = np.arange(10)    # 0부터 9까지의 숫자로 이루어진 배열
print(x)
print(x[:5])     # 0부터 4번 인덱스까지의 부분 배열
print(x[5:])     # 5 이후까지의 부분 배열
print(x[4:7])    # 4부터 6번 인덱스까지의 부분 배열
print(x[::2])    # 처음(0)부터 2씩 증가 -> [0,2,4,6,8]
print(x[1::2])   # 1번 인덱스 부터 2씩 증가하는 값 -> [1,3,5,7,9]
print(x[1:8:3])  # 1번 인덱스부터 7번인덱스까지 3씩 증가 -> [1,4,7]
print(x[::-1])   # 뒤에서부터 1씩 감소 -> [9,8,7,6,5,4,3,2,1,0]

# 0부터 9까지의 난수를 4행 5열 배열에 저장
x = np.random.randint(10, size=(4,5))
# x = np.random.randint(0,10, size=(4,5)) : 0 생략가능
print(x)

# 2개의 행과 3개의 열
print(x[:2,:3])

# 모든 행과 한개씩 걸러서 열 조회
print(x[:, ::2])

# 행을 역으로 열도 역으로 조회
print(x)
print(x[::-1, ::-1])