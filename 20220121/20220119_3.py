# 사용자로부터 점수를 입력받아서 학점을 계산하는 프로그램
# 조건  90 ~  : A
# 조건  80 ~ 89 : B
# 조건  70 ~ 79 : C
# 조건  60 ~ 69 : D
# 조건   ~   59 : F
#변수는 학점을  저장하는  변수
# 사용자 입력을 저장하는  변수
# 데이터는 input("점수 : ")
# 출력 : 00 점수는 0 학점입니다.

jumsu = int(input("점수 : "))
hakjum = 'F'
# 조건문을 이용해서 판별
if jumsu >= 90:  hakjum = 'A'
elif jumsu > 80: hakjum = 'B'
elif jumsu > 70: hakjum = 'C'
elif jumsu > 60: hakjum = 'D'
else: hakjum = 'F'

print(f"{jumsu} 점수는 {hakjum} 학점입니다.")


