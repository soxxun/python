# count = 0
# while True:
#     quite = input("계속하시겠습니까(q 는종료)")
#     if quite == 'q':
#         break

# 구구단의 단수를 입력받아서 해당하는 구구단을 출력하고... 계속....
# 해당 구구단의 출력이 끝나면 사용자에게 계속할지 물어봄
while True:
    dan = int(input("구구단의 단수를 입력하세요 : "))
    if not(2 <= dan <= 9):
        print("올바른 숫자를 입력하세요(2 ~ 9)")
        continue

    for i in range(1,10):
        print(f"{dan} x {i} = {dan * i}")

    isContinue = input("계속하시겠습니까?(y/Y)")
    if isContinue.upper() != 'Y':
        break

print("이용해 주셔서 감사합니다.")
