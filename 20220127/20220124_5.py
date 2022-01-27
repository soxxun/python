# 숫자 게임
# 규칙.... 컴퓨터가 난수를생성(1~100)
# 사용자가 맞추는 게임....
# 사용자가 추측.... 값을 입력하면.... 결과를
# com > user   45 > 2  -> 크다
# com < user   45 < 2  -> 작다
# 최종적으로 맞추면 몇번만에 맞췄는지 count값도 같이 출력

# 컴퓨터의 값은 000이고 00번 시도해서 성공했습니다.
def compareTwoNumbers(num1, num2):
    if num1 > num2:
        return False, "크다"
    elif num1 < num2:
        return False, "작다"
    else:
        return True, "같다"


import random as rd
computer = rd.randrange(1,100)
counter = 0
limit = 15
for i in range(limit):
    user = int(input("값을 예측하세요:"))
    # print(computer)
    isEqual, strs = compareTwoNumbers(computer,user)
    if isEqual:
        print(f"컴퓨터의 값은 {computer}이고 {counter}번 시도해서 성공했습니다.")
        break
    else:
        print(strs)
        counter += 1


