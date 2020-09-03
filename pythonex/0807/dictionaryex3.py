'''
Created on 2020. 8. 7.

@author: GDJ24
정렬하기
'''

import operator
dic,list={},[]
dic={"Thomas":"토마스","Edward":"에드워드","Henry":"헨리","Gothen":"고든","James":"제임스"}
#sorted: 정렬하기
#dic.items(): 내부의 튜플 객체 
#operator.itemgetter(0): 정렬의 기준을 첫번째 객체 설정 => 영문이름으로 정렬 
list =sorted(dic.items(),key=operator.itemgetter(0),reverse=True)
print(type(list))
print(list)
# 한글이름 순으로 정렬
list=sorted(dic.items(),key=operator.itemgetter(1))
print(list)
