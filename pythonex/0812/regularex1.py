'''
Created on 2020. 8. 12.

@author: GDJ24
0812/regularex1.py : 정규식 예제
'''

data = ''' 
    park 800805-1234567
    kim  700905-2345678
    choi 750905-a123456
 '''
result = []
for line in data.split("\n") :
#line : park 800805-1234567
    word_result = []
    for word in line.split(" ") :   
        # word : park 
        # word : 800805-1234567 -> len(word) == 14
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit() :  # 6번째 전까지 숫자인지, 7번째 이후 숫자인지
            word = word[:6] + "-" + "*******"  # 해당하는 경우, 800805-******* 로 변경하기
        word_result.append(word)   # word_result 에 append = [park, 800805-*******]
    result.append(" ".join(word_result))   # result 에 park와 800805-******* 이 공백을 사이에 둔 하나의 문자열로 append
print("\n".join(result))

# choi 의 경우, word[7:] 숫자가 아니므로, 해당 작업 수행 못함.