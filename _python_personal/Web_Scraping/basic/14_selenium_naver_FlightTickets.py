
# [당월 27 ~ 31] 제주도로 가는 항공편 티켓 예약하기
# 항공권 검색 후 처음 나오는 결과 선택하기
import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome() # 같은 디렉토리 내에 파일이 있으면 경로 생략 가능 (or ./chromedriver.exe)
browser.maximize_window() # 창 최대화

# 브라우저 이동 https://flight.naver.com/
url = 'https://www.naver.com/'
browser.get(url)

elem = browser.find_element_by_name('query')
elem.send_keys('네이버 항공권')
browser.find_element_by_id('search_btn').click()
browser.find_element_by_link_text('네이버 항공권').click()
time.sleep(3)

browser.switch_to.window(browser.window_handles[-1])

# Error --> stale element reference: element is not attached to the page document
# 아직 로딩되지 않아 요소를 찾지 못했다는 의미
# time.sleep() 사용 or 함수 정의
def wait_until(xpath):
    WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, xpath)))

# 가는 날 클릭
from selenium.webdriver.common.by import By # xpath 사용하기 위한 import

wait_until('//button[text() = "가는 날"]')
begin_date = browser.find_element(By.XPATH, '//button[text() = "가는 날"]')
# 슬래시 2개 : html 문서 전체에서 찾겠다는 의미
# 버튼 요소 중 '= (찾을 텍스트)'로 찾기
begin_date.click()

# 가는 날 날짜 선택
# 1. 모든 달의 27일 가져오기
wait_until('//b[text() = "27"]')
day27 = browser.find_elements(By.XPATH, '//b[text() = "27"]')
# 2. 이번달 27일 가져오기 (첫번쨰 인덱스)
day27[0].click()

# 오는 날 날짜 선택
wait_until('//b[text() = "31"]')
day31 = browser.find_elements(By.XPATH, '//b[text() = "31"]')
day31[0].click()

# === 날짜 선택 시 자동 닫힘 ===

# 도착 클릭
wait_until('//b[text() = "도착"]')
arival = browser.find_element(By.XPATH, '//b[text() = "도착"]')
arival.click()

# 버튼인데 텍스트가 '국내'인 것 찾기
wait_until('//button[text() = "국내"]')
domestic = browser.find_element(By.XPATH, '//button[text() = "국내"]')
domestic.click()

# 지금까지와 다른 방법으로 사용해보기 (일부 글자를 포함하는 요소 찾기)
wait_until('//i[contains(text(), "제주국제공항")]')
jeju = browser.find_element(By.XPATH, '//i[contains(text(), "제주국제공항")]')
jeju.click()

# 항공권 검색
# search = browser.find_element(By.XPATH, '//span[text() = "항공권 검색"]')
# search.click()

wait_until('//span[contains(text(), "항공권 검색")]')
search = browser.find_element(By.XPATH, '//span[contains(text(), "항공권 검색")]')
search.click()

# 로딩 시간 기다리는 조건 정의
# 최대 30초로 잡고 조건 명시(until)
# 만약 30초 이내에 조건에 맞는 요소가 나타나면 click, 아니면 Error
elem = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '//div[@class="domestic_Flight__sK0eA result"]')))
print(elem.text) # 텍스트 출력해보기

# 로딩 후 뜨는 검색결과 중 첫 번째 선택하기
# browser.quit()
