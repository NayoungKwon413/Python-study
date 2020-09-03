'''
Created on 2020. 8. 10.

@author: GDJ24
0810/tryex1.py : 예외 처리
'''

mystr = "파이썬 공부중입니다. 열심히 파이썬을 공부합시다."
strpos = [] # 파이썬 문자의 위치 정보 저장
index = 0
while True :
#    index = mystr.find("파이썬", index)   # index -> find 로 수정하면, 무한 루프에 빠짐 -> if문으로 break 처리
#    if index == -1 :
#        break
    try:
        index = mystr.index("파이썬", index)
        strpos.append(index)
        index += 1
    except:
        break

print("파이썬 문자의 위치:", strpos, ", 문자 갯수:", len(strpos))