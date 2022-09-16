import requests
from bs4 import BeautifulSoup

url = 'https://comic.naver.com/webtoon/weekday'
res = requests.get(url)
res.raise_for_status() # 혹시나 문제 있으면 프로그램이 바로 종료되도록 설정

soup = BeautifulSoup(res.text, 'lxml') # (url 정보, parser)

# 조건에 해당하는 모든 element 가져오기
# - 페이지 내의 class 속성인 title 정보 모두 가져오기 (네이버 웹툰 전체 목록 가져오기)
cartoons = soup.find_all('a', attrs={'class':'title'})

for i in cartoons:
    print(i.get_text())

