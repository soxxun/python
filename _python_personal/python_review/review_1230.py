
#구구단 게임
#1. 구구단게임 5회 반복
#2. 정답을 맞추면 20점
#3. 게임 종료 후 성적을 출력
'''
import random as rd

i = 1
score = 0



while i <= 5:
    a = int(rd.random() * 8) + 2
    b = int(rd.random() * 8) + 2
    value = a * b
    user = int(input(f"{a} X {b} = "))
    if user == value:
        score += 20
        print("정답!")
    else:
        score -= 20
        print("오답!")
    i += 1
print(f"축하드립니다! 총 {score}점을 획득하셨습니다!")


# 업다운 게임을 구현하려 합니다.
# 컴퓨터에게 1부터 100 사이의 정답을 생성하도록 코드를 구현한 뒤
# 사용자가 숫자를 입력하여 정답을 맞추도록 프로그래밍하세요

# <게임의 상태>
# [ 업  ] 사용자가 정답보다 낮은 값을 입력한 경우
# [ 다운 ] 사용자가 정답보다 높은 값을 입력한 경우
# [ 정답 ] 사용자가 정답과 같은 값을 입력한 경우, 게임 종료 ( 종료 지점 )

# 게임 종료시 총 입력한 횟수를 화면에 출력

#사용자가 정답을 입력하기 전까진 무한반복


import random as rd

i = 1
while True:
    num = int(rd.random() * 100) + 1
    user = int(input("1 ~ 100까지의 숫자를 입력하세요 : "))
    if user < num:
        print("[ UP ]")
    elif user > num:
        print("[ DOWN ]")
    elif user == num:
        print("[ CORRECT ! ]")
        break
    else:
        print("숫자를 정확히 입력해 주세요.")
    i += 1
print(f"축하드립니다!\n총 {i}번 시도하셨습니다.")

user = 0
num = int(random.random() * 100)+1
i = 1
while num != user:#user값과 num의 값이 똑같으면 False가 되면서 반복문 종료
    user = int(input("숫자 입력 :"))
    i += 1
    if user > num :
        print("[ 다운 ]")
    elif user < num :
        print("[ 업 ]")   
    else:
        print("[ 정답 ]")
        print("총 입력 횟수 : {}회".format(cnt))
'''

# [ 아이템 강화 시뮬레이션 ]
# 1. 아이템은 1번 강화하는데 현금 1000원이 필요하다
# 2. 아이템은 처음에 레벨이 0이다
# 3. 강화가 성공할 확률은 35% 이고 성공하면 레벨이 1 증가
# 4. 강화가 실패할 확률은 30% 이고 실패하면 레벨이 1 감소
# 5. 그 외의 경우에는 아무런 변화가 없다

# 0레벨의 아이템을 10레벨로 만들기 위해 내가 쏟아 부어야 되는 
# 현금을 계산하세요 
'''
import random as rd

lv = 0
cash = 0
i = 1

while True:
    rate = int(rd.random() * 100) + 1
    cash += 1000 # 레벨 증감 여부와는 관계없이 레벨 1 증가할 때마다 현금이 증가하기 때문에
                 # 프로그램 실행 시, 즉 레벨 10을 달성할 때까지 현금은 누적됨
    if rate <= 35:
        lv += 1
        print("강화 개이득 !")
        if lv == 0:
            print(f"축 Lv.10 달성!\n총 {cash:,d}원 차감되었습니다.")
            break
    elif rate <= 70: # (성공)1~35 ----변화없음---- 70~100(실패) *확률이 겹치지 않기 위함*
        lv -= 1
        print("강화 실패......")
    else:
        print("아무런 변화 없쥬? 개킹받쥬?")

# 정수 아닌 실수로 할 경우

import random

tot = 0
lev = 0
while lev < 10:
    rate = random.random() #0.0000~0.9999
    tot += 1000

    if rate < 0.35:
        lev += 1
        print("강화 성공!!+{}".format(lev))
    elif rate >= 0.7:
        if lev == 0:
            print("강화 실패!!0밑으로는 하락할 수 없습니다+{}".format(lev))
            continue # else 대용으로 사용하고 밑에 있는 모든 코드들을 실행하지 않고
                     # 반복문 처음으로 돌아간다.
        lev -= 1
        print("강화실패!!+{}".format(lev))
    else:
        print("아무런 변화가 없습니다+{}".format(lev))

print("강화 종료\n총 금액 : {}원".format(tot))
'''

# 369 게임 [2단계]
# 1. 1~50까지 반복
# 2. 그 안에서 해당 숫자의 369 게임 결과 출력
# 예) 1 2 짝 4 5 짝 7 8 짝 10 11 12 짝 ...
'''

i = 1
while i <= 50:
    x = i // 10 # 십의 자리(몫)
    y = i % 10 # 일의 자리(나머지)

    cnt = 0
    # 반복문이 한 번 돌 때마다 cnt = 0으로 3,6,9가 한 번에 출력되는 개수가 초기화되므로
    # 3,6,9가 한 번에 발생하는 횟수가 (아래 조건처럼) 1 아니면 2로만 반복됨
    # 따라서 초기화값을 적어준 것임
    
    if x==3 or x==6 or x==9:
        cnt += 1

    if y != 0 and y % 3 == 0:
        cnt += 1

    if cnt == 2:
        print("짝짝")
    elif cnt == 1:
        print("짝")
    else:
        print(i)
        
    i += 1
'''

# for문

string = "abcde"

for i in string:
    print(i)

for i in range(0, 5, 1): # (초기값, 끝값, 증감값) 0 ~ 4 : for i in range(5):
    print(string[i])

# 0부터 시작하면 초기값(시작값)을 적어주지 않아도 된다. (기본값) - 디폴트값
# 종료값보다 1작을때까지 반복이 된다. (미만)
# 1씩 증가될때는 증감값을 적지 않아도된다. (기본값) - 디폴트값
print()



# 0, 1, 2, 3, 4 출력

i = 0
while i < 5: # 끝값 (조건식)
    print(i)
    i += 1
print()

for i in range(5):# 초기값 : 0 끝값 : 5 ( 미만 ) 증감값 : 1 ( 생략 가능 )
    print(i)
print()

# 5, 4, 3, 2, 1, 0 출력

for i in range(5,-1,-1): # 증감값이 (-)일 때는 끝값이 1 클때까지 반복 (초과)
    print(i)
print()

#while
i = 5
while i > -1:
    print(i)
    i -= 1
print()


# for문 예제)

# 1부터 100까지의 정수
i = 0
for i in range(101):
    print(i)


# 53부터 25까지의 정수
i = 0
for i in range(53, 24, -1): # 초과값까지이기 때문에 끝값을 -1값 적어준 것
    print(i)


# 100부터 0까지의 5의 배수
i = 0

for i in range(100):
    if i % 5 == 0:
        print(i)


# A부터 Z까지의 알파벳
# A:65 Z:90 (아스키코드값)

for i in range(65, 91):
    i = chr(i)
    print(i)


# 숫자 1개를 입력받아 1부터 해당 수까지 출력

i = 0
user = int(input("숫자 입력 : "))

for i in range(user + 1):
    print(i)

