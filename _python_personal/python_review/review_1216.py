
name = "홍길동"
num = "010-3928-5247"

print("이름\t : 문소윤\n전화번호 : 010-3928-5247")
print()
print(f"이름\t:{name}\n전화번호\t:{num}")
print()
print("이름 : 문소윤\n전화번호 : 010-39285-5247")
print()

print("문소윤\r")
print("문소윤\b")

print("\"Hi\"")
print('"Hi"')
print("'Hi'")
print(":Hi:") # 다른 문자일 때는 상관없음

print('\'hello\'') # \'로 감싸주고 같은 문자열로 한 번 더 감싸주면 됨
print("문소윤\\Python\\1216") # \를 문자로 인식하고 싶을 때는 \\ 적으면 됨
print()

# end (디폴드값 : \n)
print("안녕",end="***") # '\n'(enter)의 역할이 사라짐
print("나는 문소윤이야")

print(1, end="***")
print(2)
print() # end="\n" --> 자동으로 출력됨 (기본형)
print("a")

# sep (디폴드값 : space)
print(1,2,3,4,5) # print(1,2,3,4,5,sep=" ")와 동일 (쓰나 안 쓰나 동일)
print(1,2,3,4,5,sep="\n")

# 예제 1)
print("이름 : 홍길동\n나이 : 20\n주소 : 서울특별시 강남구\n번호 : 010-1234-5247")
print()

# 함수
print(pow(2,7)) # 2의 7승
print(divmod(10,3)) # (몫, 나머지)
print(round(11.46)) # 실수 하나만 적으면 소수점 버림
print(round(11.46, 1)) # 1의자리까지 반올림
print(abs(-234)) # 절댓값
print(sum([1,2,3,4,5])) # sum함수는 꼭 [] 안에 숫자를 적어주어야 함

# 컴퓨터에서 사용되는 진법
print(0b10) # 2진수 10을 10진수로 보여주는 것
print(0o10) # 8진수 10을 10진수로 보여주는 것
print(10)
print(0x10) # 16진수 10을 10진수로 보여주는 것

print(hex(65)) # hex : 16진수 변환함수
print(hex(65), 0x41) # 동일

print(oct(8), 0o10) # oct : 8진수 변환함수 / 동일
print(oct(0x556))

print(bin(0x556), 0b10101010110, 0o2526, 1366, 0x556) # 모두 동일

# 예제 2)
print(0x3D5F)
print(hex(1024))
print(hex(3452+5785))
print(hex(sum([3452+5785])))
print()

# 0xAC + 200의 8진수 값 : 값
print("%x + %d = %o = %d" % (0xAC, 200, 0xAC + 200, 0o564))
print("{:x} + {} = {:o} = {}".format(0xAC, 200, 0xAC + 200, 0o564))
#실제로 더한 값이 372이라는 뜻
print() 

# 출력형식
# - C스타일
print("제 점수는 %d점이고 학점은 %s입니다." % (87, "B"))
# - Python
print("제 점수는 {}점이고 학점은 {}입니다.".format(87, "B"))

