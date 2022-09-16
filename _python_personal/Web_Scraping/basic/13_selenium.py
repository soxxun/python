
# Selenium
# - 웹 페이지 테스트 자동화를 할 수 있는 유명한 프레임 워크
# - 웹을 띄워 페이지 이동, 글자 입력 및 클릭 등의 이벤트 가능
# - 스크래핑을 위한 사전 작업
# - selenium & web driver 설치 필요
# - 버전 확인 --> chrome://version/ (101.0.4951.54(공식 빌드) (64비트))

'''
<터미널에서 작업>

from selenium import webdriver
browser = webdriver.Chrome(r'C:\Users\pc\Downloads\chromedriver.exe')
browser.get('http://www.daum.net')

# 검색창에 글자 쓰기
elem = browser.find_element_by_name('q')
elem.send_keys('문소윤')
# 검색 (검색 버튼 오른쪽 마우스 클릭 후 xpath 복사)
elem = browser.find_element_by_xpath('//*[@id="daumSearch"]/fieldset/div/div/button[2]')
elem.click()

# 로그인
elem = browser.find_element_by_class_name('link_login')
elem.click()

# 로그인 하기 전
browser.back() - 이전창
browser.forward() - 이후창
browser.refresh() - 새로고침

elem = browser.find_element_by_id('query')

# 키값을 직접 입력할 수 있음 (아래 import는 ENTER 하기 위함)
from selenium.webdriver.common.keys import Keys
elem.send_keys('검색할 내용')
elem.send_keys(Keys.ENTER) # 엔터

######################################################

- Tag로 정보 가져오기

elem = browser.find_elements_by_tag_name('a') (모든 elements 가져오기)

for e in elem:
    e.get_attribute('href')


browser.get('http://daum.net')
elem = browser.find_element_by_name('q')
elem.send_keys('나도 코딩')
elem.send_keys(Keys.ENTER)
browser.back()

# 검색 버튼 xpath copy --> 마우스 오른쪽 자동 붙여넣기
elem = browser.find_element_by_xpath('//*[@id="daumSearch"]/fieldset/div/div/button[2
]')

# 브라우저 종료
browser.close() --> 현재 열려있는 탭만 닫기
browser.quit() --> 모든 브라우저 닫기

터미널에서 빠져나오기
exit()
'''


