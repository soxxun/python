import requests
# res = requests.get('http://naver.com')
# res = requests.get('http://blog.naver.com/soxxun')

# 실제로 페이지 접속 시,
# 정보를 잘 받아 왔는지,
# 페이지에 대한 접속 권한은 있는지
# 페이지에 대한 정보가 없는지 등의 오류를 확인 하기 위해 아래와 같은 코드 실행해 본다.
# print(f'응답 코드 : {res.status_code}') # 200이면 정상적으로 동작했음을 의미

'''
if res.status_code == requests.codes.ok: # 200(정상)과 동일
    print('정상입니다.')
else:
    print(f'문제가 생겼습니다. [에러 코드 : {res.status_code}]')
'''

# 또 다른 방법 - 문제 발생 시 오류를 출력하고 바로 프로그램 종료
# res.raise_for_status()
# print('웹 스크래핑을 진행합니다.')

# 주로 2줄로 많이 이용
res = requests.get('http://google.com')
res.raise_for_status()

print(len(res.text))
print(res.text)

# 파일로 만들어서 보기
with open('mygoogle.html', 'w', encoding='utf-8') as f:
    f.write(res.text)