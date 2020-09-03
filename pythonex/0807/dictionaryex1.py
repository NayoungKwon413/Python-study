'''
Created on 2020. 8. 7.

@author: GDJ24
'''

singer={}
singer['이름']='트와이스' #map.put("이름","트와이스")
singer['인원수']='9명'
singer['데뷔곡']='우아하게'
singer['소속사']='JYP' #map.put("소속사","JYP")
singer['소속사']='SM' #map.put("소속사","SM") 수정

for i in singer.keys():
    print("%s => %s" % (i,singer[i]))
print(singer['이름'])
print(singer) #json형태
print(type(singer))
print(type(singer.keys()))
print(str(list(singer)))
