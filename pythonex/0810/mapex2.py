'''
Created on 2020. 8. 10.

@author: GDJ24
0810/mapex2.py : 람다를 이용하여 map 처리하기
'''

mylist = [1,2,3,4,5]
#map 을 이용하여 mylist 각각의 값에 10 더하기
add = lambda num:num+10
mylist = list(map(add,mylist))    # +10 한 값이 mylist로 대체
print(mylist)

#mylist 출력시 결과가 [10,20,30,40,50]으로 출력하기
mylist = list(map(lambda num:num-10,mylist))
mylist = list(map(lambda num:num*10,mylist))
print(mylist)


list1 = [1,2,3,4]
list2 = [10,20,30,40]
hap = lambda n1,n2:n1+n2
haplist = list(map(hap,list1,list2))
#haplist = list(map(lambda n1,n2:n1+n2,list1,list2))
print(haplist)

hap2 = lambda n1,n2,n3:n1+n2+n3
haplist2 = list(map(hap2,mylist, list1, list2))   #map(func, *iterables) : 앞에는 함수(hap2), 뒤에는 가변매개변수(list1, list2,....)
print(haplist2)