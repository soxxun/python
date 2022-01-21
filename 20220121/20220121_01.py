# 변수 두개
#number1 = 10
#number2 = 20
number1, number2 = 10, 20

print(f"number1 = {number1}  number2= {number2}")

# 두 변수의 값을 서로 교환 (swap)
number1, number2 = number2, number1

print(f"number1 = {number1}  number2= {number2}")

num1 = int(input("첫번째 숫자: "))
num2 = int(input("두번째 숫자: "))
# num1 은 num2보다 작다
if num1 > num2:  # swap
    num1, num2 = num2, num1

sum = 0
for i in range(num1, num2+1):
    sum += i

print(f"{num1} ~ {num2} 합은 {sum}")



