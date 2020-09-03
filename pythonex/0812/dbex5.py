'''
Created on 2020. 8. 12.

@author: GDJ24
0812/dbex5.py : mariadb에 데이터 추가하기
'''

import pymysql 
conn = pymysql.connect(host="localhost", port=3306, user="scott", 
                       passwd="1234", db="classdb", charset="utf8")
cur = conn.cursor()
# 튜플을 리스트형태로 집어넣음
data = [
    (11,"바나나",3000,"바나나는 길다"),
    (12, "망고", 30000, "망고는 열대과일이다"),
    (13, "배", 5000, "배는 우리나라배가 가장 맛있다")
    ]
d1,d2,d3,d4 = data[0]
print(d1,d2,d3,d4)
for i in data :
    cur.execute('''
        insert into item (id, name, price, description) values (%s,%s,%s,%s)
    ''', i)   # i : 튜플 한 묶음을 의미. 
cur.execute("select * from item")
for row in cur.fetchall() :
    print(row)
conn.rollback()   # 되돌려놓기 때문에 몇번이고 실행 가능. commit() -> 실제 db에 등록되는 것으로, 2번이상 실행시 에러