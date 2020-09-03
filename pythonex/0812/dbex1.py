'''
Created on 2020. 8. 12.

@author: GDJ24
0812/dbex1.py : sqlite db 사용하기
'''

import sqlite3   #sqlite db 모듈
dbpath = "test.sqlite"
conn = sqlite3.connect(dbpath)   # test.sqlite db에 접속(로컬에서 사용하는 db)
cur = conn.cursor()   # cursor() : db로 부터 명령을 전달하고 저장하는 객체
# executescript: 여러문장을 실행
cur.executescript('''
    drop table if exists items;
    create table items (item_id integer primary key,
        name text unique,
        price integer);
    insert into items (name, price) values ('Apple', 800);
    insert into items (name, price) values ('Orange', 500);
    insert into items (name, price) values ('Banana', 300);
 '''   )
conn.commit()   # Transaction 완료. 정상처리. / rollback() : 취소 완료
cur = conn.cursor()
cur.execute("select * from items")
item_list = cur.fetchall()   # fetchall() : select. 전체 조회해서 item_list 에 저장
print(type(item_list))
for it in item_list :
    print(it)
print(type(it))   # tuple