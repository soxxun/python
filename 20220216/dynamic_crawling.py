# > pip install selenium
# 크롬드라이버 적당한 곳에 다운받아서 풀기
from selenium import webdriver
# chromedriver.exe 하고 브라우져하고 버전이 맞을것
wd = webdriver.Chrome('D:/web/chromedriver.exe')
wd.get('https://www.daum.net/')
