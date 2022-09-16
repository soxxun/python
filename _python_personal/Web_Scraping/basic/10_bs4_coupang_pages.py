
# 최근 다섯 개의 페이지 내 모든 제품을 조회한 후
# 조건에 맞는 정보 추출하기

import requests
import re
from bs4 import BeautifulSoup

# 만약 갑자기 접속이 중단될 시
# 사람이 접속하는 것처럼 조작하기
# 아래와 같이 코드를 추가해 주면 됨
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.50"}
# res = requests.get(url, headers=headers)

for i in range(1,6): # 1~6페이지 미만
    print(f' [{i} 페이지]\n')
    url = f'https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={i}&rocketAll=false&searchIndexingToken=1=5&backgroundColor='

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

        link = item.find('a', attrs={'class':'search-product-link'})['href']

        # 평점과 평점 수 모두 존재한다는 전제
        # 평점이 4.5 이상이고, 리뷰가 100개 이상인 상품만 불러오기
        if float(rate) > 4.5 and int(rate_cnt) > 100: # 리뷰 수는 괄호로 묶여 있으므로 rate_cnt는 한 번 더 가공 처리
            # print(items.index(item) + 1, name, price+'원', rate, rate_cnt)
            print(f'{items.index(item) + 1} - 제품명 : {name}')
            print(f'\t 가격 : {price}원')
            print(f'\t 평점 : {rate}')
            print(f"\t {'http://www.coupang.com'+link}")
            print(f'\t 평점 수 : {int(rate_cnt):,}개\n{"-"*100}')
