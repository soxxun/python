
# Tuple(튜플)

# - 데이터들의 집합
# - 여러 개의 데이터들을 저장하고 관리하는 형태
# - 데이터 변경 불가능 ***
# - 같은 형태와 같은 성격의 데이터들을 보다 쉽게 관리할 수 있도록 사용

#  *선언형식
# - ()를 통해 선언
# - () 생략 가능
#   (변수처럼 하나의 공간을 만드는 것이 아니라 여러 개의 변수를 만드는 것)

# *호출
# - 인덱싱, 슬라이싱을 통해 데이터 공간 호출
# Packing - 자동으로 Tuple타입으로 저장시키는 것 ... [ () 생략 ]
# Unpacking - 자동으로 Tuple타입의 데이터를 변수 타입으로 저장시키는 것

# count(value) / index(value) --> Tuple에서 사용되는 함수
'''
tp = 1, 2, 3, 4, 5 #튜플 : packing (괄호 생략)

for i in tp :
    print(i)

print(tp)
print(type(tp))


#인덱싱
print(tp[0])
print(tp[-5])

#슬라이싱
print(tp[1:3]) # 1번째 인덱스 ~ 3(미만)번째 인덱스(2번째 인덱스)

# tp[1] = 0 # tuple은 값 변경이 불가능


tp = (1.234,123,'a',(1,2))
print(tp)

print(tp[:3])


tp = ( ( 1,2 ),
       ( 1,2,3 ),
       ( 1,2 )
    )
# print(tp)
# print(tp[0])
# print(tp[1])


#변수명[세로인덱스][가로인덱스]
print(tp[1][2])
print(tp[0][1])


#변수명[큰단위][작은단위] (쉼표를 기준으로 괄호 안 쉼표가 작은 단위)
for i in tp: # i = (1,2) / i = (1,2,3) / i = (1,2)
    for j in i : # j = 1,2 / j = 1,2,3 / j = 1,2
        print(j)

tp = 1,2,3,4,5 # Packing
a,b,c,d,e = tp # Unpacking (차례차례 하나씩 대입 *오른쪽의 값이 왼쪽에 대입)
#즉 a,b,c,d,e = 1,2,3,4,5
print(a,b,c,d,e)


tp = (1,1,2,2,2,3,3,3,3)

#튜플에서 사용되는 함수
print(tp.count(3)) # 원하는 데이터의 개수를 세주는 함수

print(tp.index(1)) # 원하는 데이터의 시작 인덱스 번호를 알려주는 함수
                   # 1이 시작하는 인덱스 번호 : 0
print(tp.__len__()) # 튜플 데이터의 개수 ( 공간의 개수 ) len(tp)

print(tp.__str__()) # 튜플을 문자열 형태로 전환
'''

# ============================================================================

# Tuple 예제)
# 아래 튜플 구조를 보고 아래에서 요구하는 값을 출력하는 코드를 작성하시오.
'''
menu = (
        ('칼국수', 6000),
        ('비빔밥', 5500),
        ('돼지국밥', 7000),
        ('돈까스', 7000),
        ('김밥', 2000),
        ('라면', 2500)
    )



# 김밥과 라면의 가격을 각각 출력하시오.
print(menu[4][1], menu[5][1]) # (변수명)[가로][세로]


# 가격이 7000원에 해당하는 메뉴를 출력하시오.
for i in menu:
    if i[1] == 7000:
        print(i[0])
        
# 이 방법도 가능
for i in range(len(menu)):
    if menu[i][1] == 7000:
        print(menu[i][0])


# 가격이 6000원에 해당하는 메뉴를 출력하시오.
for i in menu:
    if i[1] == 6000:
        print(i[0])


# 사용자 입력으로 메뉴를 입력 받아 해당하는 메뉴의 가격을 출력하시오.
user = input("메뉴 입력 : ")

#for i in menu:
#    if i[0] == user:
#        print(f"{user} 가격은 {i[1]:,d}원입니다.")
#    else:
#        print(f"메뉴명을 정확히 입력해 주세요.")
#    break

for i in range(6) :
    if menu[i][0] == user:
        print(f"{user} 가격은 {menu[i][1]:,d}원입니다.")
'''

# list에서 packing은 불가 ex) tp = 1, 2, 3, 4 *() 생략 가능,
# but 대괄호는 생략 불가 단, unpacking은 가능

# 값 변경 가능 / 튜플은 값 변경 X, 리스트는 값 변경 O
'''
ls = [1,2,3,4]
print(ls)

ls.append((6,7)) #append는 데이터의 집합 모양 그대로 list에 추가시킴
print(ls) # (6, 7)

ls.extend((6,7)) #extend는 데이터의 집합을 데이터 하나로 쪼개서 list에 추가
print(ls) # 6, 7

ls.insert(0,0) #insert(idx, 값)
print(ls)

ls.pop() #pop() - 가장 뒤에 있는 데이터 삭제 (잘라내기 기능)
print(ls)

ls.pop(5) #pop(idx) - 인덱스 안에 있는 데이터 삭제
print(ls)

ls.remove(0) #값으로 데이터 삭제
print(ls)

ls.clear() #초기화 (리스트 안에 있는 데이터를 전부 삭제)
print(ls)

#데이터가 아무것도 없는 상태이기 때문에 임의로 숫자 정의
ls = [2,3,5,6,0,7,4]

ls. sort() #오름차순 (오름차순(False)이 Default값이기 때문에 '= Flase'를 굳이 안 적어도 됨
print(ls)

ls.sort(reverse = True) #내림차순
print(ls)

ls.reverse() #다시 오름차순으로 변경
print(ls)
'''

# ================================================================================

# 아래의 리스트 구조를 보고 아래에서 요구하는 결과가 반영되도록 코드를 작성하시오.

# 비빔밥과, 돈까스의 가격을 출력하시오.

menu = [['칼국수', 6000],
        ['비빔밥', 5500],
        ['돼지국밥', 7000],
        ['돈까스', 7000],
        ['김밥', 2000],
        ['라면', 2500]]

# print(f"{menu[1][0]} : {menu[1][1]}원\n{menu[3][0]} : {menu[3][1]}원")


# 사용자 입력으로 메뉴와 가격을 입력 받아 menu 변수에 자료를 추가할 때
# 기존에 동일한 메뉴가 존재하는 경우 가격만 변경되도록 코드를 작성하시오.**
# 동일한 메뉴가 존재하지 않을 때 반복문 안에서 추가 X, 반복문이 끝나고 추가 O
'''
# 1)
check = True # 중복되는 이름이 있을 때 확인해 줄 변수 (반복문 안에서 추가 X)
             # 외부에서 if문으로 확인해야 함

food = input("메뉴 입력 : ")
price = int(input("가격 입력 : "))

for i in menu:
    if i[0] == food:
        i[1] = price # 값 변경
        check = False
        break
if check:
    menu.append([food, price]) # 대괄호 안에 리스트 형태로 묶어주기 위함
print(menu)


# 2)
for i in range(0, len(menu), 1):
    if menu[i][0] == food:
        menu[i][1] = price
        check = False # True(0)이 아닌 값으로 변경됨
        break
if check: # check가 True일 경우 추가됨 (False인 경우 위에서 break 됨)
    menu.append([food,price])
print(menu)

# 여기에서 for문 안 if문에서 else를 사용하지 않는 이유
# - 메뉴 이름이 다르면 무조건 else문으로 추가해버리는데,
# - 메뉴 이름이 같은 경우 가격만 변경해야 하기 때문에 for문 외부에서 추가를 해 주어야 함


# 메뉴가 자동으로 선택되도록 출력하는 코드를 작성하시오.

import random as rd

rand = int(rd.random() * len(menu))
print(f"{menu[rand][0]} : {menu[rand][1]}원")
'''

# ================================================================================

# 문제) 학번을 입력받아 성적 출력
#       단, 없는 학번 입력 시 예외처리
# 예)
# 학번 입력 : 1002          성적 : 11점
# 학번 입력 : 1000          해당학번은 존재하지 않습니다.
'''
hacbuns = [1001, 1002, 1003, 1004, 1005]
scores = [87, 11, 92, 14, 47]

check = -1 # T/F로 해도 됨 (True = 0 / False = 1)
hacbun = int(input("학번 입력 : "))

#for i in hacbuns:
#    if i == hacbun:
#        print(f"학번 : {hacbun}\t성적 : {scores[i]}")
#    else:
#        print("해당 학번은 존재하지 않습니다.")
#    break

# 위와 같이 하면 error --> 인덱스 번호를 알 수 없기 때문        

# 1)        
for i in range(len(hacbuns)):
    if hacbuns[i] == hacbun:
        check = i
        break
if check == -1:
    print("해당 학번은 존재하지 않습니다.")
else:
    print(f"학번 : {hacbun}\t성적 : {scores[i]}")

# 2)
for i in range(len(hacbuns)):
    if hacbuns[i] == hacbun:
        print(f"학번 : {hacbun}\t성적 : {scores[i]}")
        check = 0 # 다른 값으로 변경 (어떤 값이어도 상관없음 위에서 선언한 -1만 아니면 됨)
        break
if check == -1: # 값이 변경되지 않고 -1로 남아있으면 위 if문이 실행되지 않고,
                # 즉 없는 학번을 입력해서 외부 if문으로 빠져나온 것임
    print("해당 학번은 존재하지 않습니다.")
#else:
#    print(f"학번 : {hacbun}\t성적 : {scores[i]}")
'''

# ================================================================================

# 1 ~ 45 까지 임의의 값을 중복 없이 6개 생성하여 출력하는 코드를 작성하시오
'''
import random as rd
ls = []

# 1)

while True:
    rand = int(rd.random() * 45) + 1
    if ls.count(rand) == 0:
        ls.append(rand)
    if ls.__len__() == 6:
        break
print(ls)


# 2)

ls.clear()

while len(ls) < 6: # break가 필요 없음
    
    # 이때 6과 같다라고 써버리면 한 번 더 반복이 돌게 되므로 미만으로 써주어야 함
    
    rand = int(rd.random() * 45) + 1
    if ls.count(rand) == 0:
        ls.append(rand)
print(ls)
'''

# ================================================================================

# 빙고판 채우기
# 1 ~ 25 중복없이 5 * 5 채워져야 함
# 랜덤 인덱스 2개 (가로줄 인덱스 1, 세로줄 인덱스 1)
# 1 ~ 25 랜덤 X, 반복문 i (반복문을 1부터 25까지 반복)
# for문 X While문 O
# random 변수는 반복문 내부에 써 주어야 한번 돌 때마다 랜덤으로 출력됨
'''
import random

ls = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
    ]

# Python에서만 가능한 방법 )

i = 1
while i <= 25:
    idx1 = int(rd.random() * 5) # 0 1 2 3 4 세로인덱스
    idx2 = int(rd.random() * 5) # 0 1 2 3 4 가로인덱스
    
    if ls[idx1][idx2] == 0:
        ls[idx1][idx2] = i
        i += 1
        # 같은 인덱스가 나오면 0이 아니기 때문에,
        # i가 증가되지 않고 같은 i 값으로 처음부터 다시 반복됨
        # 그래서 ls를 1~25까지 빈 칸 없이 다 채울 수 있는 것
print(ls)


# 모든 언어에서 사용 가능한 방법 )

i = 1
while i <= 25:
    idx1 = int(rd.random() * 5)
    idx2 = int(rd.random() * 5)

    if ls[idx1][idx2] == 0:
        ls[idx1][idx2] = i
    else:
        # continue - 반복문 처음으로 다시 돌아감
        # continue 혹은 i -= 1을 골라 쓰면 됨
        i -= 1 # if문이 False가 아닌 이상 실행 안 됨
               # i = 3 일 때 False가 되어 else를 만나서 2로 감소하고
    i += 1     # 여기에서 다시 3으로 증가되어 반복문이 실행됨
print(ls)
'''

# ================================================================================

student = [
    [1001, 100],
    [1002, 30],
    [1003, 40],
    [1004, 70]
    ]

# 문제1) 합격한 사람(60점이상) 번호를 result 에 저장 후 출력
#예) result = [1001,1004,0,0]


# while문)

result = [0,0,0,0]
i = 0
idx = 0

while i < len(student):
    if student[i][1] >= 60:
        result[idx] = student[i][0]
        idx += 1
    i += 1 # 증감식 필요 ==> 반복문이 'i = 0'부터 len(student) 보다 작을 때까지 돌기 때문
print(result)


# for문)

result = [0,0,0,0]
i = 0
idx = 0

for i in student:
    if i[1] >= 60:
        result[idx] = i[0]
        idx += 1
    # i += 1 증감식 필요없음 ==> 반복문이 student (0, 1, 2, 3) 만큼만 돌기 때문
print(result)




