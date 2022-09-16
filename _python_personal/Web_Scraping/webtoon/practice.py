
import requests
from bs4 import BeautifulSoup
import re
from total_pages import *
global getTotalPages
from urllib import parse

user = input('회차 입력 : ')

for i in range(1, getTotalPages()+1):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.50"}
    url = f'https://comic.naver.com/webtoon/list?titleId=648419&weekday=mon&page={i}'
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')
    # items = soup.find_all('td', attrs={'class': 'title'})

    # viewList = soup.select('.viewList tr')  # viewList의 tr 태그
    # _ = 'https://comic.naver.com/webtoon'

    # viewList = soup.select('.viewList tr')
    viewList = soup.find_all('tr')


    # 클래스 정보가 title로 시작하는 모든 정보 가져오기
    # items = soup.find_all("td", attrs={"class":re.compile("^title")})
    # print(items)

    # user에 맞는 회차 정보의 url 얻기
    for view in viewList[3:]:  # 배너 제외
        # items = soup.find_all('td', attrs={'class': 'title'})
        title = view.select_one('.title > a').text # 제목 정보
        title_num = re.sub(r'[^0-9]', '', title[:4])
        url_info = view.select_one('.title > a').attrs.get('href')
        # page_num = re.sub(r'[^0-9]', '', url_info)[-3:]
        # page_num : 무조건 모든 숫자에서 3개를 추출함
        url_info = parse.urlparse(url_info)
        page_num = parse.parse_qs(url_info.query)['no'][0]
        print(page_num)
        # if user == title_num:
        #     print(title, page_num)

        # print(view)
        # print(title_num, page_num)
        # print(url_num)
        # if user == title[:3]:
        #     print(session_num)



