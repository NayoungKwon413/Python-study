'''
Created on 2020. 8. 7.

@author: GDJ24
ex2:배열의 값의 합과 평균을 구하는 함수 작성하기
'''
def getSum(numlist):
    return sum(numlist)
def getMean(numlist):
    print(type(numlist))
    if len(numlist)>0:
        return sum(numlist)/len(numlist)
    else:
        return 0
    #return sum(numlist)/len(numlist) if len(numlist)>0 else 0
    #return sum(numlist)/len(numlist) \  한줄을 두줄로 나타날때 \ 사용
        #if len(numlist)>0 else 0
list=[2,3,3,4,4,5,5,6,6,8,8]
print("list값의 합:",getSum(list))
print("list값의 평균:,",getMean(list))

list2=[]
print("list값의 합:",getSum(list2))
print("list값의 평균:,",getMean(list2))

tp=(2,3,3,4,4,5,5,6,6,8,8)
print("tp값의 합:",getSum(tp))
print("tp값의 평균:,",getMean(tp))

num=10
print(type(num))
num=10.5
print(type(num))