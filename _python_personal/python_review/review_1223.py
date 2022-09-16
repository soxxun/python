
# 모듈
# - 어떠한 기능들이 정의되어 있는 곳
# - 파이썬에서는 웬만한 기능들이 모두 정의되어 있음
# - 기능을 사용하려면 모듈을 지정하여 불러와서 사용하면 됨

# - 형식
# from 모듈명 import 함수명
#   - 모듈 안의 일부 기능을 사용하기 위한 방식
# inport 모듈명
#   - 모듈명 전체

# random 모듈 - 임의의 수를 구하는 함수들이 정의되어 있는 모듈
# random()
# - 0 ~ 1 미만의 실수를 구하는 함수 (디폴트값)
# - 0.0000 ~ 0.9999

# 내가 원하는 범위 안의 수 구하기
# int(random.random() * 범위 안 수의 개수) + 시작수
# 20 ~ 24 : 20, 21, 22, 23, 24 -> 5개 (범위 안 수의 개수) + 20 (시작수)

import random as rd

a = rd.random()
rand = int(rd.random() * 5) + 20
print(a, rand) # 단, random은 값을 1개만 저장하여 출력

# randint(m, n)
# - 지정한 범위 안의 임의의 수를 구하는 함수
# - m~n
rand = rd.randint(0,4) # 0, 1, 2, 4
print(rand)

# randrange(m,n,p)
# - 범위 안의 임의의 수
# - m~n 미만**
# - p는 생략 가능...p만큼 증가한 값들 중 하나
rand = rd.randrange(1,2) # 1부터 2미만이기 때문에 '1'만 출력됨
print(rand)

rand = rd.randrange(2) # 0부터 2미만 (0은 생략 가능)
print(rand)

# =======================================================================

# -02:30:00 (문자체계 : 아스키코드, 유니코드(아스키코드 포함))

# 형변환 함수
# - 문자 변환 함수 = chr(정수) -> chr(65) -> A
# - 문자 -> 유니코드값 - ord(문자) -> ord('A') -> 65
print(chr(65)) # 유니코드값 -> 문자
print(ord('A')) # 문자 -> 유니코드값

print(chr(int(rd.random() * 26) + 65)) # 영어 대문자 랜덤으로 출력
print(chr(int(rd.random() * 26) + 97)) # 영어 소문자 랜덤으로 출력
#아스키코드표 : 대문자가 65부터 시작, 소문자가 97부터 시작

# A ~ Z까지 임의의 문자 3자리 출력
# 1) random 사용
a = chr(int(rd.random() * 26) + 65) # 대문자 랜덤
b = chr(int(rd.random() * 26) + 65)
c = chr(int(rd.random() * 26) + 65)
print(a + b + c)

# 2) randrange 사용
d = chr(int(rd.randrange(65, 65 + 26)))
e = chr(int(rd.randrange(65, 65 + 26)))
f = chr(int(rd.randrange(65, 65 + 26)))
print(d + e + f)


# 영문자를 입력 받아 대/소문자를 구분한 뒤
# 소문자 --> 대문자 혹은 대문자 --> 소문자로 변환하여 출력하기
# (단, 특수문자 및 숫자 입력 시 잘못된 입력이라는 문구 표시)

user = ord(input("영문자 입력 : ")) # 'ord' (ex. A --> 65)

if 65 <= user <= 90:
    print(f"{chr(user)}의 소문자 : {chr(user+32)}")
    # 소문자 a가 97이므로 대문자 A와의 차이값인 32를 더해주어야,
    # 소문자로 변환된 값을 출력할 수 있고 chr()로 묶어주어야 문자형태로 변환 가능
elif 122 >= user >= 97:
    print(f"{chr(user)}의 소문자 : {chr(user-32)}")
else:
    print("경고! 영문자를 정확히 입력해 주세요.")
'''
# 문자로 비교
# 컴퓨터에서는 어차피 정수로 저장되어 있기 때문에
# 문자끼리의 비교도 가능
user = input("영문자 입력 : ")
if 'A' <= user <= 'z':
    print(f"{user}의 소문자 : {chr(ord(ch) + 32}")
elif 'a' <= user <= 'z':
    print(f"{user}의 소문자 : {chr(ord(ch) - 32}")
else:
    print("경고! 영문자를 정확히 입력해 주세요.")
# 입력된 값을 ord로 숫자형 변환한 후,
# 다시 그 값을 문자형 형태로 변환하여 출력한 것
'''

     


