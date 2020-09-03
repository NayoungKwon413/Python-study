'''
Created on 2020. 8. 6.

@author: GDJ24
listex2.py : 리스트의 기본함수
'''

mylist = [30,10,20]
print("리스트 : %s" % mylist)
mylist.append(40)    # append() : 또다른 요소 하나를 추가하는 함수
print("mylist.append(40) 후 리스트 : %s" % mylist)
# pop() : 스택용어. 마지막 요소 제거하고 리턴
print("pop() 메서드 결과 : %s" % mylist.pop())
print("mylist.pop() 후 리스트 : %s" % mylist)
mylist.sort()
print("mylist.sort() 후 리스트 : %s" % mylist)
mylist.reverse()
print("mylist.reverse() 후 리스트 : %s" % mylist)

print("20값의 위치 : %d" % mylist.index(20))
mylist.insert(2, 222)   #[30, 20, 10] => [30, 20, 222, 10]
print("mylist.insert(2, 222) 후 리스트 : %s" % mylist)
mylist.remove(222)
print("mylist.remove(222) 후 리스트 : %s" % mylist)

mylist.extend([77,77,99])   #extend([]) : 또다른 리스트를 추가하는 함수
print("mylist.extend([77,77,99]) 후 리스트 : %s" % mylist)
print("77값의 갯수 : %d" % mylist.count(77))

#find 함수 사용 안됨