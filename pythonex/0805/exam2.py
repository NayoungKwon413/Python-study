'''
Created on 2020. 8. 5.

@author: GDJ24
exam2.py : 초를 입력받아 몇시간 몇분 몇초인지 출력하기
'''

time = int(input("초단위로 시간을 입력하세요 : "))
print(time//3600,"시간",time%3600//60,"분",time%60, "초")
