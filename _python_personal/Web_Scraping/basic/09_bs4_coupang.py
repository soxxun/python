'''
HTTP method

우리가 http 프로토콜을 통해 서버에 요청을 보내면
서버는 그 요청에 맞는 응답을 해 준다.

요청에 포함되는 것 중 하나가 'http method'이다.

일반적으로 많이 사용하는 것이 'Get' 방식과 'Post' 방식이다.
- Get : 어떤 내용을 누구나 볼 수 있게 url에 적어서 보내는 방식
        http://www.coupang.com/np/search?minPrice=1000&maxPrice=100000&page=1
        --> 물음표 뒤는 각각 변수와 값으로 이루어져 있으며 '&' 표시로 구분됨
        --> 이러한 경우 자유롭게 변수나 값을 변경하면서 페이지를 요청할 수 있음
        --> 단, get은 한 번 전송할 때 보낼 수 있는 데이터의 양이 제한되어 있어 큰 데이터는 보내지 못함
        --> 개인정보 같은 경우는 쉽게 노출이 될 수 있어 Get 방식으로 요청하면 안됨
            --> ...?id=soxxun&pw=1234
        --> 페이지가 바뀔 때 마다 url도 바뀌면 Get 방식

- Post : url이 아닌 http 메시지 body에 숨겨 보내는 방식
        --> Get 방식 보다는 안전
        --> 데이터 양에 대한 제한이 없기 때문에 크기가 큰 데이터나 파일 업로드 같은 것도 Post 방식이 적합
            --> ex. 로그인 정보, 게시글 작성, ... etc.
        --> 페이지는 계속 변하고 있는데 url은 변함이 없는 경우는 Post 방식이라고 생각하면 됨
'''

# 쿠팡은 Get 방식으로 이루어져 있음

import requests
import re
from bs4 import BeautifulSoup

# 만약 갑자기 접속이 중단될 시
# 사람이 접속하는 것처럼 조작하기
# 아래와 같이 코드를 추가해 주면 됨
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.50"}
# res = requests.get(url, headers=headers)


url = 'https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=5&backgroundColor='

res = requests.get(url)
res.raise_for_status() # 혹시나 문제 있으면 프로그램이 바로 종료되도록 설정
soup = BeautifulSoup(res.text, "lxml")

# 'li' 태그 중에서 class 정보가 'search-product'로 시작하는 모든 정보 가져오기
items = soup.find_all("li", attrs={"class":re.compile("^search-product")})
# print(items[0].find("div", attrs={"class":"name"}).get_text())

for item in items:

    # 광고가 붙은 제품은 실제 구매자의 평가가 충분히 반영되지 않아도 상위 랭킹에 있을 수 있기 때문에
    # 광고 제품 제외
    ad_badge = item.find('span', attrs={'class':'ad-badge-text'})
    if ad_badge:
        print(items.index(item) + 1,'  <광고 상품 제외합니다.>')
        continue

    # 제품명
    name = item.find("div", attrs={"class":"name"}).get_text()

    # 애플 제품 제외
    if 'Apple' in name:
        print('  <Apple 상품 제외합니다.>')
        continue

    # 가격
    price = item.find('strong', attrs={'class':'price-value'}).get_text()

    # 평점 (평점이 없는 상품에 대해서도 처리)
    rate = item.find('em', attrs={'class':'rating'})
    if rate:
        rate = rate.get_text()
    else:
        rate = '평점 없음'
        print(items.index(item) + 1,'  <평점 없는 상품 제외합니다.>')
        continue

    # 평점 수
    rate_cnt = item.find('span', attrs={'class':'rating-total-count'})
    if rate_cnt:
        rate_cnt = rate_cnt.get_text() # 예 : (26)
        rate_cnt = rate_cnt[1:-1] # 괄호 제외
    else:
        rate_cnt = '평점 수 없음'
        print(items.index(item) + 1,'  <평점 수 없는 상품 제외합니다.>')
        continue

    # 평점과 평점 수 모두 존재한다는 전제
    # 평점이 4.5 이상이고, 리뷰가 100개 이상인 상품만 불러오기
    if float(rate) > 4.5 and int(rate_cnt) > 100: # 리뷰 수는 괄호로 묶여 있으므로 rate_cnt는 한 번 더 가공 처리
        print(items.index(item) + 1, name, price+'원', rate, rate_cnt)

