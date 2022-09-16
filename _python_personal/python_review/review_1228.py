# 12월 31일 휴강
# 나머지 하루는 녹화 안 된 날 Day??
# 총 녹화본 8개

# =========================================================================

# <중국집 주문 프로그램>
# 사용자에게 짜장면, 짬뽕 주문 수량을 입력 받아 결제 금액을 계산, 출력하기
# - 짜장면 5,000원
# - 짬뽕   6,000원

# 5그릇 이상 주문 --> 3천원 할인된 금액 출력
# 10그릇 이상 주문 --> 10% 할인 처리

# 짜장면과 짬뽕의 값이 각각 한 개 밖에 없고,
# 주문을 입력받으면 금액을 한 번만 출력하면 되기 때문에
# 반복문 필요 없음

# return은 어떻게? - 함수를 만들었을 때 사용
'''
dp = 5000
rp = 6000

ea1 = 5
ea2 = 10

rate1 = 3000
rate2 = 10

black = int(input("짜장면 개수 입력 : "))
red = int(input("짬뽕 개수 입력 : "))

tot = black + red
price = (black * dp) + (red * rp)

if tot >= ea2: # 10개 이하
    print(f"{ea1}그릇 이상 주문해 주시면 {rate2}% 할인!")
    print(f"총 {int(price - (price * 0.1)):,d}원입니다.")
    
elif tot >= ea1: # 5개 이하
    print(f"{ea1}그릇 이상 주문해 주시면 {rate1}원 할인!")
    print(f"총 {int(price - 3000):,d}원입니다.")
    
else:
    print(f"총 {price:,d}원입니다.")
'''

# =========================================================================

# 주사위 2개 던지는 코드 구현하기
# 두 개의 주사위 합계에 따라 아래와 같이 코드 구현
'''
import random as rd
# rd.randint(1,6) <-- 이렇게도 가능
rand1 = int(rd.random() * 6) + 1
rand2 = int(rd.random() * 6) + 1
tot = rand1 + rand2

print(rand1, rand2)

if rand1 == rand2:
    print("더블!")
    # 더블이 짝을 포함하기 때문에 짝을 먼저 써버리면 더블도 짝으로 출력됨
elif tot % 2 == 0:
    print("짝!")
else:
    print("홀!")

#만약 짝부터 비교를 꼭 하고 싶다면?

if tot % 2 == 0 and rand1 != rand2:
    print("짝!")
elif tot % 2 == 0:
    print("짝!")
else:
    print("홀!")
'''
# =========================================================================
'''
# 문자열
string = "abcd"

# 1) 인덱싱
print(string[0])
print(string[-4]) # 뒤에서부터 접근할 때
# 거꾸로 접근할 때는 0 대신 -1

# 2) __len__() 데이터 공간의 개수를 구하는 함수
print(string.__len__()) # a b c d --> 4개
# len(연속적인 공간
print(len(string))

# 슬라이싱
# - 인덱싱을 이용하여 부분적으로 잘라내는 것
# - [m:n] - m부터 n 이전(미만)
print(string[1:3])
print(string[1:])
print(string[:4])

# find(str)
# - 문자열에서 특정 문자열을 찾아 해당하는 문자의 인덱스값을 반환하는 함수
# - 없으면 -1을 반환, 있으면 그 인덱스값을 반환
msg = "     abcdefgaa     "
print(msg.find("f"))
print(msg.find("a"))
print(msg.find("aa"))

# count(str)
# - 문자열에서 특정 문자열을 찾아서 해당 문자열의 수를 반환하는 함수
print(msg.count(" ")) # 10
print(msg.count("a")) # 3

# lower - 대 -> 소
# upper - 소 -> 대
# swapcase - 대 -> 소 / 소 -> 대
a = "AbCdEfG"
print(a.swapcase())

# isupper() - 문자열이 대문자면 True, 대문자 이외에 다른 게 있으면 False
# islower() - 문자열이 소문자면 True, 소문자 이외에 다른 게 있으면 False
print(a.islower())


# - s를 소문자로 만든 다음에 islower()을 사용하여 True 반환하기
a = a.lower()
print(a.islower())


# 공백 제거 함수
# - strip() : 앞 뒤 제거
# - istrip() : 좌측 제거
# - rstrip() : 우측 제거
print(msg.strip())
print(msg.lstrip())
print(msg.rstrip())

# replace(old, new)
# - old 문자열을 new 문자열로 치환하는 함수
print(msg.replace("ab","가나"))
print(msg.replace("ab","가나").strip()) # 치환 후 공백 제거
print(msg.strip().replace("ab","가나")) # 공백 제거 후 치환

# split(str)
# - 문자열을 특정 문자열로 분리하는 함수
msg = "빨-주-노/초-파/남-보"
print(msg.split("-"))

ls = msg.split("-")
print(ls[2].split("/")) # 두번째 인덱스에서 "/"를 기준으로 값 반환하기
'''
# =========================================================================
'''
# 다음 조건을 보고 회원가입을 위한
# 프로그램 코드 작성하시오.
# 아이디는 반드시 10자리 이상
# 패스워드는 반드시 8 ~ 16자리 이상
# 패스워드에 아이디가 포함되면 안됨

id = input("아이디 입력 : ")

if len(id) >= 10:
    pw = input("비밀번호 입력 : ")
    if 8 > len(pw) > 16:
        print("비밀번호는 8자에서 16자 사이로 입력해 주세요.")
    elif pw.find(pw) >= 0: # True이면 인덱스 번호를 반환하므로 무조건 0 이상이기 때문
            print("비밀번호에 아이디를 포함할 수 없습니다.")
    else:
        print(f"\n입력하신 아이디와 비밀번호는 아래와 같습니다.\n"
              f"ID : {id}\nPassword : {pw}")
        
else:
    print("아이디를 10자리 이상 입력해 주세요.")
'''
# =========================================================================

# 반복문

# while : 반복할 횟수가 일정하지 않을 때
# for : 반복할 횟수가 일정할 때

# While
# - 반복할 횟수가 무한일 때
# - 반복할 횟수를 모를 대
# - 간단한 조건식 이용할 때

# break : while, for문에서 실행 흐름으로부터 벗어나려 할 때 사용하는 흐름 제어문
'''
i = 1
while True:
    print(i)
    if i == 9:
        break
    i += 1
print()

i = 1
while i <= 9:
    print(i)
    i += 1
print()

# 1부터 100까지의 정수 중 짝수(혹은 홀수)만 출력
i = 1
while True:
    if i % 2 == 0:
        print(i)
    if i == 100:
        break
    i += 1

i = 1
while i <= 100:
    if i % 2 == 0:
        print(i)
    i += 1

# 10부터 1까지 반복하여 6 ~ 3 거꾸로 출력
i = 10
while True:
    if 3 <= i <= 6:
        print(i)
    if i == 1:
        break
    i -= 1 # 숫자가 거꾸로 출력됨

while i >= 1:
    if 3 <= i <= 6:
        print(i)
    i -= 1
'''

# 1 ~ 5까지의 합 출력
'''
i = 1
result = 0
while True:
  # if i <= 5: => 여기에 if는 있어도 되고 없어도 됨
    result += i
  # print(result) <-- 과정을 다 출력하고 싶으면 여기에 print
    if i == 5:
        print(result) # 결과값 한 번만 출력
        break
    i += 1

i = 0
result = 0
while i <= 5:
    result += i
    i += 1
print(result)


# 1 ~ 10까지 반복해 3 미만 7 이상만 출력

i = 1
while i <= 10:
    if i < 3 or i >= 7:
        print(i)
    i += 1

i = 1
while True:
    if i < 3 or i >= 7:
        print(i)
    if i == 10:
        break
    i += 1
'''

# 문제 2의 조건에 맞는 수들의 합 출력 (37)
'''
i = 1
result = 0
while i <= 10:
    if i < 3 or i >= 7:
        result += i
    i += 1
print(result)
    

i = 1
result = 0
while True:
    if i < 3 or i >= 7:
        result += i
    if i == 10:
        break
    i += 1
print(result)
'''

# 문제 2의 조건에 맞는 수들의 개수 출력 (6)
# 1)

i = 1
result = 0
su = []

while i <= 10:
    if i < 3 or i >= 7:
        result += i
        su.append(result)
    i += 1
print(len(su))


# 2)
i = 1
su = 0

while True:
    if i < 3 or i >= 7:
        su += 1
    if i == 10:
        break
    i += 1
print(su)


# 3)
i = 1
su = 0

while i <= 10:
    if i < 3 or i >= 7:
        su += 1
    i += 1
print(su)

