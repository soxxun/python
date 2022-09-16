
import glob
import tkinter
import re
import requests
from urllib import parse
from total_pages import *
global getTotalPages


def Beautiful_Goonbari():
    try:
        user = input('회차 입력 : ')

        # 원하는 회차 이름 출력
        for i in range(1, getTotalPages()+1):
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.50"}
            url = f'https://comic.naver.com/webtoon/list?titleId=648419&weekday=mon&page={i}'
            res = requests.get(url, headers=headers)
            res.raise_for_status()
            soup = BeautifulSoup(res.text, 'lxml')
            # items = soup.find_all('td', attrs={'class':'title'})

            viewList = soup.find_all('tr')
            # viewList = soup.select('.viewList tr') 도 가능

            for view in viewList[3:]:  # 배너 제외
                title = view.select_one('.title > a').text  # 제목 정보
                title_num = re.sub(r'[^0-9]', '', title[:4])

                # url의 'no'의 파라미터값 추출 (&no=)
                url_info = view.select_one('.title > a').attrs.get('href')
                url_info = parse.urlparse(url_info)
                page_num = parse.parse_qs(url_info.query)['no'][0]

                # 입력한 회차의 url 불러오기 및 이미지 찾기
                if user == title_num:
                    print('\n',title)
                    images_url = f'https://comic.naver.com/webtoon/detail?titleId=648419&no={page_num}&weekday=mon'
                    webtoon = requests.get(images_url, headers=headers)
                    webtoon.raise_for_status()
                    parser = BeautifulSoup(webtoon.text, 'lxml')
                    images = parser.find_all('img', attrs={'alt':'comic content'})

                    # 찾은 이미지 저장하기
                    for idx, image in enumerate(images):
                        image_url = image['src']
                        # print(idx, image_url)

                        image_res = requests.get(image_url, headers=headers)
                        image_res.raise_for_status()

                        with open(f'webtoon_images_{idx}.jpg', 'wb') as f:
                            images = f.write(image_res.content)
                else:
                    pass

        return images
    except Exception as e:
        print(e, '회차 정보를 잘못 입력하셨습니다.')
Beautiful_Goonbari()


from merge_image import merge_image
merge_image()

from delete_files import *
delete_jpg_png()

# 외부 함수를 함수 내에서 호출할 시 -> UnboundLocalError --> global '함수/변수명'
