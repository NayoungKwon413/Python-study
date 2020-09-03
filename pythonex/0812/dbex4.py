'''
Created on 2020. 8. 12.

@author: GDJ24
0812/dbex4.py : mariadb 사용하기
'''

import pymysql  # pip install pymysql 

conn = pymysql.connect(host="localhost", port=3306, user="scott", 
                       passwd="1234", db="classdb", charset="utf8")
try :
    cur = conn.cursor()   # 명령 전달 객체
    cur.execute("select * from item")
    while True :
        row = cur.fetchone()   # 한개의 레코드만 조회
        if row == None :   # 조회된 레코드가 없는 경우 -> break
            break
        print(row)
#    for row in cur.fetchall() :   # 모든 레코드 조회
#        print(row[0], row[1], row[2])   # print(row) : 모든 컬럼의 값들 출력
finally:
    cur.close()
    conn.close()