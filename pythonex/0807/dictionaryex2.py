'''
Created on 2020. 8. 7.

@author: GDJ24
'''

foods={"떡볶이":"오뎅","짜장면":"단무지","라면":"김치","맥주":"치킨"}
for i in foods.keys() : #map.keySet()
    print("%s => %s" % (i,foods[i]))

#화면에서 음식을 입력받아 궁합음식 출력하기
while True:
    myfood = input(str(list(foods.keys()))+"중 음식이름 입력하세요:")
    if myfood == "종료":
        print("등록된 음식 갯수:"+str(len(foods))) #키의갯수
        print("좋아하는 음식:"+str(list(foods.keys())))
        print("궁합음식:"+str(list(foods.values()))) #map.values()
        print(list(foods.items())) #map.entrySet()
        break
    if myfood in foods: #myfood 값이 foods의 key에 존재?
        print("<%s> 궁합은식은 <%s>입니다." % (myfood,foods[myfood]))
    else:
        print("등록된 음식이 아닙니다.")
        yn = input("좋아하는 음식으로 등록하시겠습니까?(y)")
        if yn=='y' or yn=='Y':
            f = input("궁합음식을 입력하세요:")
            foods[myfood] = f
        
