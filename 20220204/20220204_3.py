# 정수를입력받아서 제곱을 구함
try:
    number = int(input("정수 : "))
except:
    pass
else:
    print(f"number의 제곱은 {number ** 2}")

# ValueError: invalid literal for int() with base 10: 'adsfadfads'
# IndexError: list index out of range
try:
    list_a = [1, 5, 7, 8, 9]
    index = int(input("원하는 리스트의 인덱스를 입력하세요(0 ~ 4) : "))
    list_a[index]
except Exception as e:
    print(f"예외발생 : {e}")
else:
    print(f"index = {index}  list_a[index] = {list_a[index]}")


print("프로그램 종료")

