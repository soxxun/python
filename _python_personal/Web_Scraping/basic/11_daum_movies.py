
import requests
from bs4 import BeautifulSoup

for year in range(2015, 2020):
    url = f'https://search.daum.net/search?w=tot&q={year}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR'
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')

    images = soup.find_all('img', attrs={'class': 'thumb_img'})

    for idx, image in enumerate(images):
        image_url = image['src']
        if image_url.startswith('//'):
            image_url = 'https:' + image_url
        print(image_url)

        # 페이지에 있는 정보를 파일로 저장하기
        image_res = requests.get(image_url)
        image_res.raise_for_status()

        # 리소스(image_res)가 가지고 있는 content 정보(이미지)를 파일로 쓰기
        with open(f'movie_{year}_{idx+1}.jpg', "wb") as f:
            f.write(image_res.content)

        # 상위 5개의 이미지만 다운로드 하기
        if idx >= 4:
            break



