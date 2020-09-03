'''
Created on 2020. 8. 6.

@author: GDJ24
listex1.py : 리스트 예제(배열)
  파이썬 리스트(list) => []
          딕셔너리(자바의 Map) => {key, value}
      set(중복허용X. 집합)   => {value}  
          튜플(상수처리된 리스트)  => ()
'''

a = [0,0,0,0]
b = []
print(a, len(a))
print(b, len(b))
suma, sumb = 0,0
for i in range(0, len(a)) : 
    a[i] = int(input(str(i+1)+"번째 값 : "))   #str() : 문자열로 변경 -> 입력받은 값 int로 다시 변경해 a[]배열에 추가
    suma += a[i]
    b.append(a[i])   # b 리스트에 값을 추가. 자바함수의 add 함수랑 같은 함수
    sumb += b[i]
print(a, len(a))
print(b, len(b))
print("a 리스트 합계 : ", suma)
print("b 리스트 합계 : ", sumb)
print(a[::-1])