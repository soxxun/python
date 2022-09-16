import requests

url = 'http://soxxun.tistory.com'

# my user Agent
# http://www.whatismybrowser.com/what-is-my-user-agent
# 접속하는 브라우저에 다라 user agent가 달라진다.

# 크롬 user agent 가져오기
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36'}
res = requests.get(url, headers=headers) # 페이지 접속 시 사용자 정의 user agent값을 넘겨 줌
res.raise_for_status()

# 파일로 만들어서 보기
with open('soxxun.html', 'w', encoding='utf-8') as f:
    f.write(res.text)

# 잘 검색됨
# 이제 문제 없이 자유롭게 웹 스크래핑을 할 수 있게 됨



