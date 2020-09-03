'''
Created on 2020. 8. 11.

@author: GDJ24
0811/classex4.py : 클래스에서 사용되는 메서드
'''

class Line :
    length = 0
    def __init__(self, length):
        self.length = length
    
    # 자바의 toString 메서드 기능
    def __repr__(self):
        return "선의 길이:" + str(self.length)
    
    # 객체들 간 + 연산자 사용 시 호출되는 메서드 -> 연산자 오버로딩
    def __add__(self, other):
        print("더하기 연산자가 호출되었습니다.")
        return self.length + other.length
    
    # 객체들 간 < 연산자 사용시 호출되는 메서드
    def __lt__(self, other):
        print("< 연산자가 호출되었습니다.")
        return self.length < other.length
    
    # 객체들 간 > 연산자 사용시 호출되는 메서드
    def __gt__(self, other):
        print("> 연산자가 호출되었습니다.")
        return self.length > other.length
    
    # 객체들 간 == 연산자 사용시 호출되는 메서드
    def __eq__(self, other):
        print("== 연산자가 호출되었습니다.")
        return self.length == other.length
    
    # 소멸자 : 객체가 소멸될 때 호출되는 메서드
    def __del__(self):   
        print(self.length, "길이의 선이 제거되었습니다.")

myline1 = Line(200)  # __init__ 호출, 생성자
myline2 = Line(100)  # __init__ 호출, 생성자
print(myline1)   # __repr__ 호출. toString() 메서드와 같은 기능.
print(myline2)   # __repr__ 호출
print("두 선의 길이의 합 : ", myline1+myline2)   # __add__ 호출

# 두 선의 길이 비교하기
if myline1.length < myline2.length :
    print("myline2 선이 더 깁니다.")
elif myline1.length == myline2.length :  
    print("myline1과 myline2 선의 길이는 같습니다.")
else :
    print("myline1 선이 더 깁니다.")
    
if myline1 < myline2 :     # __lt__ 호출, False
    print("myline2 선이 더 깁니다.")
elif myline1 == myline2 :  # __eq__ 호출, False
    print("myline1과 myline2 선의 길이는 같습니다.")
elif myline1 > myline2 :   # __gt__ 호출, True -> myline1 선이 더 깁니다. 출력
    print("myline1 선이 더 깁니다.")
    
# 프로그램 종료 시점 -> 자원을 반납해야 함. 즉, 객체가 모두 소멸됨. -> 소멸자(__del__) 호출
