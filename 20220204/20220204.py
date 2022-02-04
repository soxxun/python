# 예측할수없는 오류가 발생했을때 프로그램을 정상적으로 실행하도록 도와주는 것
# number = int(input("정수"))
# print(f"number ={number}")

#전통적인 예외처리는 예측가능한 예외를 전부 기술...
number = input("정수")
# if number.isdigit():
#     number = int(number)
#     print(f"number ={number}")
# else:
#     print("잘못 입력했습니다. ")
try:
    number = int(number)
    print(f"number ={number}")
except:
    print("잘못 입력했습니다. ")

print("프로그램 종료")

