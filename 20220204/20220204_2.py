# 정수를입력받아서 제곱을 구함
number = input("정수 : ")
if number.isdigit():
    number = int(number)
    print(f"number의 제곱은 {number**2}")
list_a = [1, 5, 7, 8, 9]
index = input("원하는 리스트의 인덱스를 입력하세요(0 ~ 5) : ")
if index.isdigit() and  (0 <= int(index) <= 4 ):
    index = int(index)
    print(f"index = {index}  list_a[index] = {list_a[index]}")

print("프로그램 종료")