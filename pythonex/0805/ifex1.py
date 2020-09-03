'''
Created on 2020. 8. 5.

@author: GDJ24
ifex1.py : if 조건문 예제
'''

score = 85
if score >= 90 : 
    print("A학점")
else : 
    if score >= 80 :
        print("B학점")
    else : 
        if score >= 70 :
            print("C학점")
        else : 
            if score >= 60 :
                print("D학점")
            else :
                print("F학점")
    
print("if elif 구문으로 변경하기")
if score >= 90 : 
    print("A학점")
elif score >= 80 :
    print("B학점")
elif score >= 70 :
    print("C학점")
elif score >= 60 :
    print("D학점")
else :
    print("F학점")