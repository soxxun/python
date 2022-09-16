
# C언어 / Python

# 소수점 자리 지정
print("%f, %.2f" % (1.234, 1.234))
print("{:f}, {:.10f}".format(1.234,1.234))

# 고정길이 출력
# - C언어
print("|%5d|" % (10)) # 숫자 포함 다섯 칸 확보 및 오른쪽 정렬
print("|%-5d|" % (10)) # 숫자 포함 다섯 칸 확보 및 왼쪽 정렬

# - Python
print("/{:5}/".format(10)) # 우측정렬 : 디폴트값
print("/{:<5}/".format(10)) # 좌측정렬 : <
print("/{:^6}/".format(10)) # 중앙정렬 :  ^ (숫자 두자리 제외 양쪽 두칸 두칸씩 띄어진 것)
print(f"/{10:<5}/")

print()

su = 123.123
print("{:,}".format(1000000))
print(f"{1000000:,}") # 정수 / 실수 단위 구분
print(f"{1000000:,.2f}") # + 소수점 자릿수까지 지정
print(f"{int(su)}")

print("|{:>20}|".format("{:,}".format(1000000)))
# .format("100,000")을 위처럼 써 준 것
# format : 변경시켜 준다는 의미를 지녔으므로 위와 같이 사용 가능

# 데이터 타입 변환 함수
# - bool() 논리형으로 변환
# - int() 정수형으로 변환
# - float() 실수형으로 변환
# - str() 문자열로 변환

x, y, z = -1, 0, "abc"
print(bool(x))
print(bool(y)) # 0만 False
print(bool(z))

# C언어에서는 입력되는 데이터에 한해서 무조건 0을 거짓으로 취급
# 0 이외 모든 것은 True로 출력


# 예제 1) '110.520' 출력하시오
x, y, z = '100', 10.5, 20
print(str(int(x) + y ) + str(z))


# 나머지 연산
# 1) 홀짝 구분, 배수, 약수
# 2) 정수의 자릿수 구분
# 3) 랜덤수의 범위 제한

n1, n2 = 500, -511
print(n1 % 2) #0 (짝수는 2로 나누면 무조건 0)
print(n2 % 2) #1 (홀수는 2로 나누면 무조건 1)

num = 123
print(num // 100) #1 (100의 자릿수)
print(num % 100) #23 (10의 자릿수, 1의 자릿수)
print(num % 100 // 10) #2 (1의 자릿수) *100으로 나눈 나머지 23, 23을 10으로 나눈 몫, 즉 10의 자릿값
print(num % 100 % 10) #3 (1의 자릿수) *100으로 나눈 나머지 23, 23을 10으로 나눈 나머지, 즉 10의 자릿값

# 예제 2) '21년 12월 19일'과 같이 출력
birth = 211217

# 1)
year = birth // 10000
month = birth % 10000 // 100
date = birth % 100
print("{}년 {}월 {}일".format(year, month, date))
print(f"{year}년 {month}월 {date}일")

# 2)
date = birth % 100 # 17
birth = birth // 100 # 1221
month = birth % 100 # 12
year = birth // 100 # 21
print("{}년 {}월 {}일".format(year, month, date))
print(f"{year}년 {month}월 {date}일")
print()

# 비교연산자는 T/F로 반환
print(not True) # False
print(not False) # True

word1 = "apple"
word2 = "apple"
print(word1 == word2)

#예제 3)

# 내 지갑에 10000원
# 컵라면 1500, 콜라 1000
# 1) 거스름돈 얼마?
# 2) 500원 개수, 100원의 개수

mine =  10000
ramen = 1500
coke = 1000
change = mine - (ramen + coke)
five = change // 500
one = change // 100

print(f"잔돈은 {change}원입니다.")
print(f"500원짜리 갯수는 {five}개이고, 100원짜리 갯수는 {one}개입니다.")








