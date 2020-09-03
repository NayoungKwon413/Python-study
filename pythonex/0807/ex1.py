'''
Created on 2020. 8. 7.

@author: GDJ24
나라와 수도를 등록하고 화면에 나라이름을 입력받아 해당 나라의 수도를 출력하기
    등록된 나라가 아닌경우 수도를 입력받아 등록하기
    나라 입력시 종료 입력되면 프로그램 종료
    종료시 등록된 모든 나라와 수도 정보를 화면에 출력하기
'''
country = {"대한민국":"서울","영국":"런던","중국":"베이징","미국":"워싱턴","대만":"타이페이","일본":"도쿄"}
while True:
    cnt = input(str(list(country.keys()))+"중 수도를 알고 싶은 나라는?:")
    if cnt == '종료':
        for i in range(country.keys()):
            print("%s => %s" % (i,country[i]))
    if cnt in country:
        print("<%s>의 수도는 <%s>입니다." % (cnt,country[cnt]))
    else:
        print("등록된 나라가 아닙니다.")
        yn = input("수도를 등록하시겠습니까?(y/n)")
        if yn=='y' or yn=='Y':
            f = input("수도를 입력하세요:")
            country[cnt] = f
        else:
            continue       
    