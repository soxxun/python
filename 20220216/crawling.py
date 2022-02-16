from bs4 import BeautifulSoup as bt
#연습용 html 작성
html = '<h1 id="title">크롤링 연습</h1>' \
       '<div class="top"><ul class="menu">' \
       '<li><a href=http://https://www.daum.net/ class="login">로그인 </a>' \
       '</li></ul><ul class="brand"><li><a href="https://www.daum.net/>다음<li>' \
       '<a href="https://www.daum.net/">다음</a></li></ul></div>'
soup = bt(html,"html.parser")  # html을 파싱
print(soup.prettify()) # 내용 확인
# tag를 이용한 추출
# print(soup.h1)
# print(soup.div)
# print(soup.ul)
# print(soup.li)
# print(soup.a)
tag_a = soup.a
tag_a_all =  soup.find_all('a')
# 속성을 이용한 추출
print(tag_a)
print(tag_a.attrs)
# print(tag_a.attrs['href'])
# print(tag_a.attrs['class'])
print(tag_a['href'])
print(tag_a['class'])

tag_url = soup.find('ul',attrs={'class':'brand'})
print(tag_url)

title = soup.find(id='title')
print(title)
print(title.string)

li_list =  soup.select("div>ul.brand>li")
print(li_list)
for li in li_list:
    print(li.string)

# 크롤링 허용 여부 확인하기
# 크롤링할 주소 /robots.txt
# 1. 파일이 없으면 허용
# 모든 접근 금지
# User-agent: *
# Disallow: /

# 모든 접근을 허용
# User-agent: *
# Allow: /
#또는
# User-agent: *
# Disallow:

#특정 디렉토리만 접근금지
# User-agent: *
# Disallow: /login/
# Disallow: /admin/

