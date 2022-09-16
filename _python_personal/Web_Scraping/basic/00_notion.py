

# 웹 스크래핑 : 웹 페이지 내에서 원하는 부분만 가져오는 것
# 웹 크롤링 : 주어진 웹 페이지 내에 있는 링크를 따라가며 모든 내용을 가져오는 것

# 웹 구성요소
# - HTML
# - CSS
# - JS(Java Script)

# HTML (Hyper Text Markup Language) - 웹 페이지를 만들 때 사용하는 언어

'''
<html></html> 열고 닫음 즉 print의 괄호와 같은 역할로, 닫아줄 때 슬래쉬를 넣어주면 됨
<head></head> : 홈페이지의 제목이나, 문서의 선행작업 등
<body></body> : 문서의 본문 내용 등


<html>
    <head></head>
    <body></body>
</html>
'''

# HTML 작성 시 <head></head> 안에 '<meta charset="utf-8">'를 써주어야 utf-8로 인식하여 한글 패치가 제대로 됨
# <input>은 슬래쉬로 닫지 않아도 됨

# html, head, body 등은 '태그'라고 불리우며,
# 내부에 쓰이는 input, type 등은 '어트리뷰트'라고 불린다. 또한 이러한 속성들이 모여 하나의 element를 구성하는 것이다.

# HTML에 대하여 자세히 배우고 싶다면
# 1. http://www.w3school.com
# 2. run HTML

# xpath : html 문서를 갔을 때 어떠한 태그나 속성값을 찾고자 할 때 그 경로를 의미

# 크롬
# - 인터넷의 한 종류로, 구글에서 만든 웹 브라우저
# - xpath를 구하기가 비교적 쉽기 때문에 개발자가 가장 많이 사용

# 웹 스크래핑 시 웹에서 원하는 정보(html 문서 정보)를 추출하기 위해 --> requests 라이브러리

a = 12345
b = "12345"
print(f'{a:,}')
print(f'{int(b):,}')