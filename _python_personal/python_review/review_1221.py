
score = 50
# flag = (0 <= grade) and (score <= 100) <-- 이 식을 간소화 한 것이 아래식
flag = 0 <= score <= 100
print(flag)

num = 101
flag = (num % 2 == 0) and '짝수' or '홀수'
# 위 조건이 참이면 and 옆 문자열이 실행
# 위 조건이 거짓이면 or 옆 문자열이 실행
print(flag)

# and로 연결된 두 조건식 모두 True => True 출력
age = 23
gender = "남성"
goToArmy = (age >= 20) and (gender == "남성")
print("현역 입영 대상입니까? ",goToArmy)
print()

cash = 5000
card = 0
canGoHomeByTaxi = (cash >= 3800) or (card == 1)
print("택시타고 집에 가기 :",canGoHomeByTaxi)

# 저장한 점수가 0점에 100점 사이이면 True를 출력
score = int(input("점수 입력 : "))
scoreRange = (0 <= score <= 100)
print(scoreRange)

# 나이에 따라서 성인/미성년자 여부를 문자열 변수에 저장하고
# 화면 출력하세요.
age = int(input("나이 입력 : "))
# 성인이 참일 때 경우
flag = (age < 20) and "미성년자" or "성인"
print(flag)
# 미성년자가 참일 때의 경우
flag = (age >= 20) and "성인" or "미성년자"
print(flag)

name = input("학생 이름 : ")
kor = int(input("국어점수 입력 : "))
eng = int(input("영어점수 입력 : "))
math = int(input("수학점수 입력 : "))
tot = kor + eng + math
avg = tot // 3
          
print("출력 결과")
print("="*20," 학생 정보 ", "="*20)
# print('''이름\t국어\t영어\t수학\t합계\t평균
# {}\t{}\t{}\t{}\t{}\t{:.2f}'''.format(name, kor, eng, math, tot, avg))

print("이름", "국어", "영어", "수학", "합계", "평균",sep = "\t")
print("{}\t{}\t{}\t{}\t{}\t{:.2f}".format(name, kor, eng, math, tot, avg))
''''''

salary = int(input("월급 입력 : "))
annual = int((salary * 12) - (salary * 0.1))
print(f"당신의 연봉은 {annual*10000:,d}원 입니다.")

# 숫자 2개 입력하고 서로 교환(교체) 출력
a,b = int(input("첫번째 숫자 입력 : ")), int(input("두번째 숫자 입력 : "))
c = a # c = 1
a = b # a = 2
b = c # b = 1
print(b, a) # 1, 2

# Python
a, b = b, a
print(a, b) # 1, 2


