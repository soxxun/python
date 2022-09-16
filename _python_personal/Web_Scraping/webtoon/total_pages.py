
from bs4 import BeautifulSoup
import requests

def getTotalPages():
    page = 1
    last_page = 0

    while True:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.50"}
        url = f'https://comic.naver.com/webtoon/list?titleId=648419&weekday=mon&page={str(page)}'
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, 'lxml')

        viewList = soup.select('.viewList tr') # viewList의 tr 태그
        _ = 'https://comic.naver.com/webtoon'

        for view in viewList[3:]: # 배너 제외
            imgSrc = view.select_one('a > img').attrs.get('src') # 썸네일 정보
            title = view.select_one('.title > a').text
            link = _ + view.select_one('.title > a').attrs.get('href')
            # rating = view.select_one('.rating_type > strong').text
            # date = view.select_one('td.num').text
            # print(imgSrc)
            # print(title)
            # print(link)
            # print(rating)
            # print(date)
        if soup.select_one('a.next') == None: # next가 없다면
            last_page += page
            # print('last page was ' + str(page))
            break
        page = page + 1

    return last_page

getTotalPages()