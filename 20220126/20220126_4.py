# 함수

# 구구단 함수....
# dan = 6
# for i in range(1,10):
#     print(f"{dan} x {i} = {dan * i}")

# 만들기
def gogodan(dan):
    for i in range(1,10):
        print(f"{dan} x {i} = {dan * i}")

#사용하기  이왕이면.. 2~9단까지 개별 단을 출력하는 함수를 이용해서 다 출력해 보자
for i in range(2,10):
    gogodan(i)
    print("----------------------------------------------------")

# 리스트를 전달받아서 최대값을 출력하는 함수
# getMaxList
def getMaxList(list_a):
    # print(f"max value = {max(list_a)}")
    return max(list_a)


list_a = [1,2,5,1,5,1,4,1,4,5,1,4,50]
maxValue = getMaxList(list_a)
print(maxValue)
print( getMaxList(list_a) )

# 키보드로부터 값을 받아서 변수에 저장 (사용자가 숫자만 입력 잘 한다고 가정하고)
# 0 ~ 100  사이의 값이 안들어오면 다시 입력하라고 요청하고 입력을 받는다


import util

# 리펙토링의 한 모습을 보고 계십니다...  Refactoring
count = 1
while True:
    # 구구단 단수를 입력한다
    dan = util.inputGuguDan()
    # 구구단을 출력한다.   -- 비지니스 로직
    util.gugudanProcess(dan)
    # 계속할지 물어본다
    if not util.isContinue():
        break
    count += 1

print(f"총 이용 횟수는 {count}번 입니다.")










