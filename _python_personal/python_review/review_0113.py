
# Day10
# 함수 선언
'''
def say_hello() : # 함수 선언 - 매개변수 X
    # 함수 안에 적히는 코드 (내부)
    print("안녕하세요")

# 함수 밖에 적히는 코드 (외부)
say_hello() #함수 호출 - 인자값 X


def sum_test(a,b) : # 매개변수 a,b
    if a == 10 :
        return None # return 함수종료
    return a + b

one = sum_test(11,12)
print(one) # 23


# star함수
# 인자값을 보낸만큼 반복돌려서 별을 출력

def star(n):
    for i in range(0,n):
        print("*",end="")
    print() # --> 없으면 아래 출력값들이 모두 붙어 나옴

star(5)
star(6)
star(2)
'''
# ========================================================================
'''
#리턴 없는 함수

#문제 1) 1부터 5까지 합을 출력하는 함수

def sumValue():
    tot = 0
    for i in range(1,6):
        tot += i
    print(tot)

sumValue() # 15


#문제 2) x부터 y까지의 합을 출력하는 함수

def sum_value(x,y):
    tot = 0
    for i in range(x,y+1):
        tot += i
    print(tot)

sum_value(3,8) # 33


#문제 3) 리스트 nums를 전달받아 최대값을 출력해주는 함수

# 정수 형태의 값으로 출력 
num = [ 10 , 87 , 23 , 19 , 3 ]

def maxValue(list_a):
    maxN = 0
    for i in list_a:
        if i > maxN:
            maxN = i
    print(maxN)

maxValue(num) # 87

# 리스트 형태로 추가
def max_Value(list_a):
    maxN = []
    list_a = int(max(list_a))
    maxN.append(list_a)
    print(maxN)

max_Value(num) # [87]
'''
# ========================================================================
'''
nums = [10, 20, 30, 40, 50]

# 문제 1) 전체 합을 반환해 주는 함수
# 전체 합을 구한 뒤 리턴

def sumAll(n):
    tot = 0
    for i in n:
        tot += i
    return tot

print(sumAll(nums)) # 150



# 문제 2) 4의 배수의 합을 반환해주는 함수
# 4의 배수 합을 구한 뒤 리턴

def sumValue(n):
    tot = 0
    for i in n:
        if i % 4 == 0:
            tot += i
    return tot

print(sumValue(nums)) # 60



# 문제 3) 4의 배수만 리스트 타입으로 반환해주는 함수
# 4의 배수를 리스트에 다 추가한 후 리턴

def listValue(n):
    tot = []
    for i in n:
        if i % 4 == 0:
            tot.append(i)
    return tot

print(listValue(nums)) # [20, 40]
'''
# ========================================================================
''''
# 문제 1) score 리스트에 1~100사이의 랜덤 값 5개를 저장해서 리턴해주는 함수

import random as rd
score = []

def randScore(score):
    for i in range(5):
        su = int(rd.random() * 100) + 1
        score.append(su)
    return score

sc = randScore(score)
print(sc)


# 문제 2) 성적이 60점 이상이면 합격.

#         합격생들의 방번호(index)와 성적을 리턴해주는 함수
#         [[인덱스, 성적],[인덱스,성적]]

ls = []
def lsScore(arr):
    for i in range(len(arr)):
        if arr[i] >= 60:
            ls.append([i, arr[i]])
    return ls

ls = lsScore(sc)
print(ls)


# 문제 3) 1등 학생의 방번호(index)를 리턴해주는 함수
# - 함수를 이용한 방법

def maxIndex(arr):
    maxScore = max(arr) # 'arr'의 리스트 내 가장 큰 수 반환
    maxIdx = arr.index(maxScore) # maxScore와 동일한 값의 인덱스 번호 반환

    return maxIdx

maxIdx = maxIndex(sc)
print(maxIdx)

# 반복문 이용한 방법

def maxIndex(arr):
    maxScore = 0
    maxIdx = 0 # 인덱스가 0부터 시작하므로 변수를 0으로 두면
                # 코드가 잘못돼도 오류를 인식하지 못하기 때문에 -1로 둠
    for i in range(len(arr)):
        if maxScore < arr[i]: # 돌아갈 때마다 숫자 크기 비교
            maxScore = arr[i] # 순차적으로 넣은 숫자 보다 크면 변수에 대입
            maxIdx = i # 대입된 숫자의 인덱스 번호 maxIdx 변수에 대입
                       # (인덱스 번호를 큰 값 마다 받아온 것)
    return maxIdx

maxIdx = maxIndex(sc)
print(maxIdx)
'''
# ========================================================================

'''
함수(Function)
 - 독립적인 기능을 실행하는 작은 프로그램
 - 프로그램을 각 기능별로 분류하여 구조적인 효율성을 추구한다.
 
함수의 특징
 - 함수는 독립적으로 실행한다.
 - 함수는 고유한 기능을 지닌다.
 - 함수는 매개변수를 가질 수 있다. ( 외부에서 함수로 받아오는 값 )
 - 함수는 반환값을 가질 수 있다. ( 함수에서 외부로 보내주는 값 )
 - 재사용, 관리 및 수정이 편리하다.

함수의 정의
 - 함수의 이름 및 기능을 정의한것
 - 함수의 형식
   def 함수명(매개변수):
      코드정의
      코드정의

  - 함수명
   - 함수를 호출할때 사용하는 이름
   - 함수의 기능이 연상되는 단어로 이름을 지어준다.

  - 매개변수 ( 외부에서 함수로 받아오는 값 ) - 함수에서의 입장
   - 함수를 실행할때 전달받을 인자의 형태
   - 함수가 실행할때 필요한 데이터

  - 반환값 ( 함수에서 외부로 보내주는 값 )
   -  함수가 실행되고 종료될때 반환하는 값
   - 함수 안에서 만들어진 결과물을 다른 외부에서 사용할때 돌려주는 값
   - return을 통해서 반환시킨다

** return **
 - 함수의 종료
 - while문의 break와 비슷하게 생각하면된다.
 - 함수의 반환값이 있는 경우 return 뒤에 적어주면 된다.
 - return을 통해서 반환되는 값은 단 하나만 가능하다.

함수의 호출
 - 함수명 : 사용하려는 기능이 정의된 함수이름
 - 인자값 : 사용하려는 함수의 매개변수로 들어가는 데이터..** ( 외부에서 함수로 보내주는 값 )
  - 함수의 매개변수의 형식과 개수, 순서에 맞도록 인자값을 전달해야한다.
 - 형식
   함수명(인자값,인자값..)
'''

# <출력 결과>

# 요금 투입 : 1000
# =============== 커피 자판기 ================
# 1. 커피(200원) 2.코코아(250원) 3.반환 4.종료
# 메뉴 선택 : 1
# 커피가 나왔습니다.
# 현재 금액은 800원 입니다.

# =============== 커피 자판기 ================
# 1. 커피(200원) 2.코코아(250원) 3.반환 4.종료
# 메뉴 선택 : 2
# 코코아가 나왔습니다
# 현재 금액은 550원 입니다.

# =============== 커피 자판기 ================
# 1. 커피(200원) 2.코코아(250원) 3.반환 4.종료
# 메뉴 선택 : 3
# 550원을 반환합니다.

# 요금투입 : 
# =============== 커피 자판기 ================
# 1. 커피(200원) 2.코코아(250원) 3.반환 4.종료
# 메뉴 선택 : 4
# 자판기를 종료 합니다.
'''
price = 0

def esc():
    print("종료합니다.")
    exit(0)

def coffee():
    global price
    if price < 200:
        print("금액이 부족합니다.")
        addInputCheck()
    else:
        print("커피가 나왔습니다.")
        price -= 200
        print(f"현재 금액은 {price}원 입니다.")
  # return price 전역변수를 사용했으므로 price 변수를
  #              값을 다시 외부로 반환해 줄 필요가 없음

def cocoa(price):
    if price < 250:
        print("금액이 부족합니다.")
        addInputCheck()
    else:
        print("코코아가 나왔습니다.")
        price -= 250
        print(f"현재 금액은 {price}원 입니다.")
    return price

def returns(price):
    global check # 전역변수 - check라는 변수이름을 찾아서 함수가 종료되어도
                 #            그 값이 사라지지 않고 보존되어 있음
    print(f"{price}원을 반환합니다.\n")
    price = 0
    while True: # 금액을 다시 투입하는 반복문
        add = input("모자란 금액을 투입하시겠습니까?")
        if add == 'y':
            check = False # retrun price로 이동
            break
        elif add == 'n':
            print("자판기를 종료합니다.")
            esc()
        else:
            print("잘못된 입력")
        return price

while True:
    price += int(input("요금 투입 : ")) # 여기서부터 다시 실행됨
    check = True # (다시 돌아왔을 때 False이기 때문) 다시 True로 변환
    while check: # 전역변수로 이용할 check 변수
                 
        print("="*15," 커피 자판기 ","="*15,"\n",
              "1.커피(200원)   2.코코아(250원)\n",
              "3.반환          4.종료\n")
        select = int(input("메뉴 선택 : "))

        if select == 1:
            price = coffee(price)
        elif select == 2:
            price = cocoa(price)
        elif select == 3:
            price = returns(price)
        elif select == 4:
            esc()
        else:
            print("잘못된 입력입니다!")
'''

# 전역변수(price, check)를 이용한 방법

price = 0

def esc():
    print("종료합니다.")
    exit(0)

def addInputCheck(): # 자판기가 종료되었을 때 금액을 추가 투입할 것인지
                     # 남은 금액을 저장하고 모자란 금액 투입
    global check
    while True:
        add = input("모자란 금액을 투입하시겠습니까?")
        if add == 'y':
            check = False
            break
        elif add == 'n':
            print("자판기를 종료합니다.")
            esc()
        else:
            print("잘못된 입력")

def coffee():
    global price
    if price < 200:
        print("금액이 부족합니다.")
        addInputCheck()
    else:
        print("커피가 나왔습니다.")
        price -= 200
        print(f"현재 금액은 {price}원 입니다.")
      # return price

def cocoa():
    global price
    if price < 250:
        print("금액이 부족합니다.")
        addInputCheck()
    else:
        print("코코아가 나왔습니다.")
        price -= 250
        print(f"현재 금액은 {price}원 입니다.")
      # return price

def returns():
    global price, check
    
    print(f"{price}원을 반환합니다.\n")
    price = 0 # 잔돈 반환 후 price : 0원
    while True: # 금액을 다시 투입하는 반복문
        add = input("금액을 다시 투입하시겠습니까?")
        if add == 'y':
            check = False # retrun price로 이동
            break
        elif add == 'n':
            print("자판기를 종료합니다.")
            esc()
        else:
            print("잘못된 입력")
      # return price

while True:
    price += int(input("요금 투입 : ")) # 여기서부터 다시 실행됨
    check = True # (다시 돌아왔을 때 False이기 때문) 다시 True로 변환
    while check: # 전역변수로 이용할 check 변수
        
        print("="*15," 커피 자판기 ","="*15,"\n",
              "1.커피(200원)   2.코코아(250원)\n",
              "3.반환          4.종료\n")
        select = int(input("메뉴 선택 : "))

        if select == 1:
            coffee() # coffee함수에서 매개변수로 넘겨주던 price를 반환하지 않고
                     # 전역변수로 사용했기 때문에 매개변수 값은 비워두어야 함
        elif select == 2:
            cocoa()
        elif select == 3:
            returns()
        elif select == 4:
            esc()
        else:
            print("잘못된 입력입니다!")

