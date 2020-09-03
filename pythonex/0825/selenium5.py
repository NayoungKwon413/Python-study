'''
Created on 2020. 8. 25.

@author: GDJ24
0825/selenium5.py : 
'''
import time
from selenium import webdriver

# 크롬 브라우저 로드
driver = webdriver.Chrome("D:/20200703back/20200522back/20200522back/setup/chromedriver_win32/chromedriver")
time.sleep(1)
# url 설정
driver.get("https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com")
id = input("네이버 아이디를 입력하세요:")
# javascript 실행
driver.execute_script("document.getElementsByName('id')[0].value='"+id+"'")
pw = input("네이버 비밀번호를 입력하세요:")
driver.execute_script("document.getElementsByName('pw')[0].value='"+pw+"'")
# find_element_by_xpath : xpath 이용하여 지정한 태그 객체에 접근
# click() : 클릭이벤트 발생 => 버튼 클릭효과
driver.find_element_by_xpath('//*[@id="log.login"]').click()   # xpath의 형식, @:속성을 의미.  f12=>해당부분 copy xPath=>paste
time.sleep(1)
# 쇼핑 영역 클릭
driver.find_element_by_xpath('//*[@id="NM_FAVORITE"]/div[1]/ul[1]/li[5]/a').click()
time.sleep(1)
# My 쇼핑 영역 클릭
driver.find_element_by_xpath('//*[@id="_myPageWrapper"]/a').click()
time.sleep(1)
# 주문확인/배송조회 영역 클릭
driver.find_element_by_xpath('//*[@id="_myPageWrapper"]/div/div[3]/ul[2]/li[2]/a').click()
time.sleep(1)
# 주문정보 보기
products = driver.find_elements_by_css_selector(".goods_pay_section")
for product in products:
    print("-", product.text)
time.sleep(2)
driver.quit()