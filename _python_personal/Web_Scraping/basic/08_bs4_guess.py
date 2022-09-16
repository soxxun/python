
import requests
from bs4 import BeautifulSoup

url = 'https://comic.naver.com/webtoon/list?titleId=648419&weekday=mon'
res = requests.get(url)
res.raise_for_status() # 혹시나 문제 있으면 프로그램이 바로 종료되도록 설정

soup = BeautifulSoup(res.text, 'lxml') # (url 정보, parser)

# cartoons = soup.find_all("td", attrs={"class":"title"})
# title = cartoons[0].a.get_text()
# print(title)

# 제목과 링크 정보 함께 출력하여 바로 이동할 수 있는 코드 작성해보기
# - 링크 --> a 태그의 속성 정보
# link = cartoons[0].a['href'] # url 주소 앞 부분이 잘림
# print('https://comic.naver.com' + link) # 나머지 부분 복사해서 앞에 붙여넣기



# for문 이용하여 모든 회차 정보 가져오기
'''
for cartoon in cartoons:
    title = cartoon.a.get_text()
    link = 'https://comic.naver.com' + cartoon.a['href']
    print(f'{title} : {link}\n')
'''


# 각 회차의 평점 평균
cartoons = soup.find_all("div", attrs={"class":"rating_type"})

total_rates = 0
for cartoon in cartoons:
    # 문서상 cartoon.strong 으로 바로 적어도 될 것 같지만 일단 find 이용하기
    rate = cartoon.find("strong").get_text() # 처음으로 만나는 strong 객체
    print(rate)
    total_rates += float(rate)
print(f'전체 점수 : {total_rates}')
print(f'평균 점수 : {total_rates / len(cartoons)}')


# 터미널에서 'python'을 적어준 뒤 바로바로 실행하면서 결과를 볼 수도 있음
# python은 interpreter 언어라고 함
# 보통 프로그래밍 언어는 compile 방식과 interpreter 방식이 있음
#   compile 방식은 코드를 작성하면 컴퓨터가 알아들을 수 있는 언어로 한 번 변환이 되어 실행됨
#   interpreting 방식은 한 줄씩 바로바로 실행 가능하여 결과도 즉시 볼 수 있고 그때그때마다 수정도 가능함 (like 동시통역)
# 오류 시에도 계속 실행할 수 있음

# 이렇게 하면 코드를 추가할 때마다 새로 실행하여 그때마다 다시 웹 페이지에서 html을 불러오면서 소요되는 시간을 줄일 수 있음
# 종료(원래 터미널로 빠져나오기) -> exit()

# 참고로 bs4는 한글 문서가 제공되어 있음
# Google -> 'Beautifulsoup' 검색
# 이 문서는 한국어 번역도 가능합니다.
# 예시 코드와 설명 참고!