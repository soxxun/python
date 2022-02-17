from selenium import webdriver
from bs4 import BeautifulSoup
import time
# chromedriver.exe 하고 브라우져하고 버전이 맞을것
# WebDriver 객체생성
wd = webdriver.Chrome('D:/web/chromedriver.exe')
#웹페이지 연결
coffeBean = 'https://www.coffeebeankorea.com/store/store.asp'
wd.get(coffeBean)
html = wd.page_source
# html parser를 위한 BeautifulSoup 객체 생성
soup =  BeautifulSoup(html,"html.parser")
# print(soup.prettify())
#매장 정보 추출
store_name =  soup.select("div.store_txt>h2")
print(store_name)
wd.close()