# 구구단 함수
# parameter :
# return : 출력할 단
def inputGuguDan():
    value = int(input("구구단 단수를 입력하세요:"))
    while not (2 <= value <= 9):
        print("2 과 9사이의 값을 입력하세요")
        value = int(input("구구단 단수를 입력하세요:"))
    return value

# 주석....
def gugudanProcess(dan):
    for i in range(1, 10):
        print(f"{dan} x {i} = {dan * i}")

#주석....
def isContinue():
    isContinueValue = input("계속하시겠습니까(y/Y)")
    if isContinueValue.upper() == 'Y':
        return True
    else:
        return False