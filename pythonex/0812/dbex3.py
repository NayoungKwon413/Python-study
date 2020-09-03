'''
Created on 2020. 8. 12.

@author: GDJ24
0812/dbex3.py
'''

# sqlite3 : 내부적으로 가지고 있는 db. 가벼우나 성능이 좋지 못함.
import sqlite3
dbpath = "test.sqlite"
con = sqlite3.connect(dbpath)
cur = con.cursor()

while True :
    data1 = input("사용자 ID => ")
    if data1 == '' :
        break
    data2 = input("사용자 이름 => ")
    data3 = input("이메일 => ")
    data4 = input("출생 연도 => ")
    sql = "insert into usertable values ('" \
    + data1 + "', '" + data2 + "', '" + data3 + "', " + data4 + ")"
    cur.execute(sql)
    con.commit()
    
cur = con.cursor()
cur.execute("select * from usertable")
list = cur.fetchall()
for row in list :
    print(row)
con.close()