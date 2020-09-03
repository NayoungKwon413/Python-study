'''
Created on 2020. 8. 11.

@author: GDJ24
0811/classex3.py : 상속 예제. 오버라이딩 예제

오버라이딩 : 부모 클래스의 요소들 재정의하는 것
다중상속 가능
'''

class Car : 
    speed = 0
    door = 3
    def upSpeed(self, value):
        self.speed += value
        print("현재 속도(부모클래스): %d" % self.speed)
    
class Sedan(Car):   # class 클래스이름(부모클래스이름) : 상속표현  -> Car 라는 부모클래스를 상속받음
    pass            # pass : 추가 멤버가 없음

class Truck(Car):
    def upSpeed(self, value):   # 오버라이딩
        self.speed += value
        if self.speed > 150 :
            self.speed = 150
        print("현재 속도(자손클래스): %d" % self.speed)

class Container : 
    room = 1

class MovingCar(Container, Car):   # 다중상속
    pass 


sedan1 = Sedan()
truck1 = Truck()
print("트럭:", end="")
truck1.upSpeed(200)
print("승용차:", end="")
sedan1.upSpeed(200)

mcar = MovingCar()
mcar.upSpeed(60)
print("이동차량의 방갯수:", mcar.room, ", 문의 갯수:", mcar.door)   # room = Container 에서, door = Car 에서 가져옴

