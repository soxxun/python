# 1. 1 ~ N 까지의 합을 구하시오  f(5)  1+2+3+4+5
# 2 두개의 값을 받아서 사용자가 + - x / 기호를 입력하면  f(10 ,20,+)   10+20
# 3 숫자를 입력받아서 입력받은 숫자들끼리 합을 구하는 함수 f(1,5,2,7)  f(1,2)  가변 매개변수
# 4. 절대값을 구하는 함수  f(-123)   123   abs()
# 5. 리스트의 길이를 구하는 함수  len()이라는 내장함수를 사용하지 않고

# 1번문제의 답
def sumN(n):
    hap = 0
    for i in range(1,n+1):
        hap += i
    return hap

def calcTwoNum(x, y, op):
    result = 0
    if op == '+':
        result = x+y
    elif op == '-':
        result = x + y
    elif op == '*':
        result = x * y
    elif op == '/':
        result = x / y
    else:
        result = 0
    return result

def numbersSum(*numbers):
    result = 0
    for i in numbers:
        result += i
    return result

def myAbs(data):
    result = data
    if data < 0 :
        result = data * -1
    return result

def myLen(lists):
    result = 0
    for i in lists:
        result += 1
    return result

name = "이규영"
dic_a = {'a':100, 'b':200}
print(f"dic_a is length = {myLen(dic_a)}")

a = -125
print(a)
print(abs(a))
print(a * -1)

