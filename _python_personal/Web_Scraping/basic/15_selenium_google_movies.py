import requests
from bs4 import BeautifulSoup

url = 'https://play.google.com/store/movies/collection/cluster?clp=0g4XChUKD3RvcHNlbGxpbmdfcGFpZBAHGAQ%3D:S:ANO1ljJvXQM&gsr=ChrSDhcKFQoPdG9wc2VsbGluZ19wYWlkEAcYBA%3D%3D:S:ANO1ljK7jAA&hl=ko&gl=US'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.50",
    'Accept-Language':'ko-KR,ko' # 한글 언어로 된 페이지 요청 가능 / html 내 한글 검색 가능
    }

res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, 'lxml')

movies = soup.find_all('div', attrs={'class':'ImZGtf mpg5gc'})
# print(len(movies)) # 동적 페이지 --> selenium 활용
# print(movies)

# =============== html 문서 생성 =====================

# with open('movie.html', 'w', encoding='utf8') as f:
#     # f.write(res.text)
#     f.write(soup.prettify()) # html 문서를 예쁘게 출력
#     # 문서 내에서 검색이 안됨 (--> default 브라우저에서는 모두 영문이기 때문)
#     # 한글 페이지 잘 받아와야 함 --> user agent (headers)

# ===================================================

# 순위 매기기
lank = 1
for movie in movies:
    title = movie.find('div', {'class':'WsMG1c nnK0zc'}).get_text()
    print(f'{lank}. {title}')
    lank += 1

# selenium 이용하여 로딩되는 모든 순위 가져오기





