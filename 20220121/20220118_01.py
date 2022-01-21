# 주석
# 모든 프로그램은 반드시 주석이 있어야 한다...
# print("안녕하세요. 첫 수업입니다.")

import keyword
print(keyword.kwlist)

# 프린트 함수 연습
number = 150  # 변수 선언 및 초기화
print(100)
print(100+200)
print(number)   # 변수 출력(number)
print(number+200)
number2 = number  # 새로운 변수에 값을 할당 및 초기화
print(number2)
number2 = 300

# 초기화--> 값을 최초로 할당

# 변수를 처음 사용하고 값을 초기화 하지 않으면.. 기존에 있는 변수로 생각하기때문에
# 에러
# number3

print("hello \"python\"")
print('hello "python"')

print("abc\ndef")
print("abc\tdef")

message = "동해물과\n백두산이\n마르고\n닳도록"
print(message)

print("----------------------")
print("""\
동해물과
백두산이
마르고
닿도록\
""")
print("----------------------")