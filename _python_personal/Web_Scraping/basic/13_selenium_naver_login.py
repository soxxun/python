import time

from selenium import webdriver
browser = webdriver.Chrome(r'C:\Users\pc\Downloads\chromedriver.exe') # 같은 디렉토리 내에 파일이 있으면 경로 생략 가능 (or ./chromedriver.exe)

# 네이버 이동
browser.get('http://www.naver.com')

# 홈페이지 로그인 버튼 클릭
elem = browser.find_element_by_class_name('link_login')
elem.click()

# id / pw 입력
# 입력만 하면 끝이기 때문에 따로 변수명으로 받을 필요 없음
time.sleep(3)
browser.find_element_by_id('id').send_keys('soxxun')
browser.find_element_by_id('pw').send_keys('sodo5247')
time.sleep(3)
# time.sleep을 해주지 않으면 네이버 자체에서 자동입력으로 인식하여 로그인 실패

# 로그인 버튼 클릭
browser.find_element_by_id('log.login').click()

# 자동입력 방지문자 입력 요청 시
# 지우고 다시 입력
# browser.find_element_by_id('id').clear()

# browser.find_element_by_id('id').send_keys('soxxun')
# browser.find_element_by_id('pw').send_keys('sodo5247')

# html 정보 출력
print(browser.page_source)

# 브라우저 종료
input('종료하려면 Enter 키를 입력하세요.') # 사용자 입력 대기
browser.quit()

