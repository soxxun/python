import requests
from bs4 import BeautifulSoup

url = 'https://comic.naver.com/webtoon/weekday'
res = requests.get(url)
res.raise_for_status() # 혹시나 문제 있으면 프로그램이 바로 종료되도록 설정

soup = BeautifulSoup(res.text, 'lxml')
# 가져온 html 문서를 lxml을 통해서 beautifulsoup 객체로 만들어 준 것
# soup이란 변수가 모든 정보를 담고 있게 됨

# print(soup.title)
# print(soup.title.get_text()) # 문자열만 가져오기

# soup 객체가 가지고 있는 모든 정보 중에서 '첫 번째로 발견되는 a element' 출력
# 메인메뉴로 바로가기
# print(soup.a)
#
# # a element의 속성 정보 출력
# print(soup.a.attrs)
#
# # 'href'의 값만 가져오고 싶을 때
# # --> soup.['원하는 attribute 값']
# print(soup.a["href"]) # a element의 href 속성 '값' 정보 출력

# < 웹 스크래핑 하려는 대상 페이지에 대한 정보가 없을 때 >
#  - a 태그 중 어떤 정보를 찾고 싶을 때 --> 일단 웹 개발자 도구에서 찾고싶은 정보의 유니크 값 복사해오기
#  - soup 객체에 있는 모든 내용 중에서 a 태그에 해당하는 첫 번째 엘리먼트를 가져옴
#    (태그명, attrs={"조건"})

'''
print(soup.find("span", attrs={"class":"mask"})) # 기기괴괴
# id가 따로 없고 class 정보만 있어, class 속성을 활용함


# mask는 하나밖에 없는 고유한 정보이기 때문에 앞에 태그명을 생략해 주어도 동일한 속성값을 출력해 줌
# 그러나 찾으려는 값이 두 개 이상일 때는 앞에 태그명을 명시해 주어야 보다 정확한 정보를 얻을 수가 있음
print(soup.find( attrs={"class":"mask"}))


# 웹툰 실시간 20대 인기순위
print(soup.find('li', attrs={'class':'rank01'}).get_text()) # 이름만 가져오기

rank01 = soup.find('li', attrs={'class':'rank01'})
print(rank01.a) # soup 변수와 동일한 역할 수행 --> a element의 정보만 출력
'''

# 부모, 자식, 형제로 이동
'''
# next
print(rank01.get_text())

print(rank01.next_sibling) # 아무것도 출력 안 됨
print(rank01.next_sibling.next_sibling.get_text()) # 두 번 하니까 출력됨
# 태그 사이 개행 정보가 있어 그럴 수 있음
# 즉 줄바꿈이 있어 출력이 한 번에 안 될 수 있으므로 next_sibling을 두 번 해 주면 됨

rank02 = rank01.next_sibling.next_sibling # 변수에 get_text를 해 주면 AttributeError
rank03 = rank02.next_sibling.next_sibling
print(rank03.a.get_text())

# previous
rank02 = rank03.previous_sibling.previous_sibling
print(rank02.a.get_text())

# parent
print(rank01.parent)
'''

# next_sibling을 두 번 적어주는 대신 find를 이용하여
# 조건에 해당되는 정보만 찾기
'''
rank02 = rank01.find_next_sibling('li')
print(rank02.a.get_text())

rank03 = rank02.find_next_sibling('li')
print(rank03.a.get_text())

rank02 = rank03.find_previous_sibling('li')
print(rank02.a.get_text())


# 한 번에 모든 정보 찾기 - siblings
# rank01을 기준으로 그 다음의 정보 모두 가져오기
print(rank01.find_next_siblings('li'))
'''



# text : 열고 닫는 사이의 텍스트
'''
<a
id="recommand_titleName_3"
href="/webtoon/detail?titleId=731130&amp;no=144"
class="tit" title="이두나!">이두나!</a>

--> 이두나! 가 text인 것
'''
webtoon = soup.find('a', text='이두나!')
print(webtoon.get_text())

