'''
Created on 2020. 8. 20.

@author: GDJ24
'''

import matplotlib.pyplot as plt   # pip install ggplot

# 한글 폰트 설정하기
plt.rcParams["font.family"] = "NanumGothic"   # 한글 폰트 지정해야 한글 출력 가능함
plt.rcParams["font.size"] = 8

plt.style.use("ggplot")
subjects = ["자바", "JSP", "스프링", "하둡", "파이썬"]
print(range(len(subjects)))
subjects_index = range(len(subjects))   # 0,1,2,3,4 => 인덱스 표현
print(type(subjects))
scores = [65,90,85,60,95]   # 수치 데이터
# 그래프 출력
fig = plt.figure()    # fig : 그래프 그릴 공간. 도화지
ax1 = fig.add_subplot(1,1,1)   # 도화지 분리. 1개의 도화지에 여러개의 그림 가능.
                               # 현재 프로그램은 1개의 그림만 그림.
                               # 1행1열 분리 => 그림 한 개
                               # 1 => 1번째 그림
# bar: 막대그래프 설정
ax1.bar(subjects_index,scores,align="center",color="darkblue")
# axis : 축 설정
ax1.xaxis.set_ticks_position("bottom")
ax1.yaxis.set_ticks_position("left")
# x축 설정
plt.xticks(subjects_index, subjects, rotation=0, fontsize="small")
plt.xlabel("Subject")  # x축 내용
plt.ylabel("Score")    # y축 내용
plt.title("Class Score")
# 그래프를 img 파일로 저장
plt.savefig("bar_plot.png", dpi=400, bbox_inches="tight")
plt.show()   # 화면에 출력