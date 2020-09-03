'''
Created on 2020. 8. 11.

@author: GDJ24
0811/classex1.py : 클래스 예제
                                멤버, 멤버메서드, 생성자
                                기본생성자  : 생성자를 구현하지 않으면 시스템에서 제공하는 생성자
                  def __init__(self) : => 기본생성자 형태(self = this : 자기참조변수)
                  v1="", v2=0 : 매개변수의 기본값
'''

class Car :
    # 멤버변수
    color = ""   
    speed = 0
    
    # 생성자 : 생성자 없을 경우, 시스템에서 기본생성자 자동 부여
    # 생성자의 이름 : __init__
    def __init__(self, v1="", v2=0):
        self.color = v1
        self.speed = v2
    
    # 멤버 메서드
    def upSpeed(self, value):    # self : 없는 것처럼 생각해야 ... 시스템이 알아서 채워주는 값(자기참조)
        self.speed += value
    def downSpeed(self, value):
        self.speed -= value
    
myCar1 = Car()  # __init__(self, v1="", v2=0), 객체화
myCar1.color = "빨강"
myCar1.speed = 0
myCar1.upSpeed(30)    # value = 30 
print("자동차1 색상: %s, 속도: %dkm" % (myCar1.color, myCar1.speed))    

myCar2 = Car("파랑", 50)
myCar2.downSpeed(10)
print("자동차2 색상: %s, 속도: %dkm" % (myCar2.color, myCar2.speed))    

myCar3 = Car("노랑")   # v2 값이 안들어왔어도, 기본 값 0
myCar3.upSpeed(20)
print("자동차3 색상: %s, 속도: %dkm" % (myCar3.color, myCar3.speed))    