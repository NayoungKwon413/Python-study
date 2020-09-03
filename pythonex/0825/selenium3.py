'''
Created on 2020. 8. 25.

@author: GDJ24
0825/selenium3.py : selenium 을 이용해 url 연결
                    url 에서 제공되는 html 의 내용을 BeautifulSoup 모듈로 파싱
                    pandas 모듈을 이용하여 csv 파일로 생성
'''
import time
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome("D:/20200703back/20200522back/20200522back/setup/chromedriver_win32/chromedriver") 
driver.get('http://oscar.go.com/winners')
time.sleep(1)

# url이 전달하는 html 내용
html = driver.page_source
print(html)
soup = BeautifulSoup(html, 'html.parser')
category = soup.select('bls-winners-list > ul > li > div.winners-list__info > a')
movie = soup.select('bls-winners-list > ul > li > div.winners-list__info > h3 > a')
producer = soup.select('bls-winners-list > ul > li > div.winners-list__info > p')
oscars_2020 = []
# zip : 리스트 merge => 튜플
for item in zip(category, movie, producer):   # item : 튜플
    oscars_2020.append(
        # dictionary 객체로 생성
        {
            'category' : item[0].text,
            'movie'    : item[1].text,
            'producer' : item[2].text
            }
    )
data = pd.DataFrame(oscars_2020)  # 판다스 객체로 생성
print(data)
data.to_csv('oscars_2020.csv')
driver.quit()