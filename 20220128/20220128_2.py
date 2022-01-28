def sum_all(start, end):
    # check value
    if start > end:  # 1000, 10
        start, end = end, start
    output = 0
    for i in range(start, end+1):
        output += i
    return output

print(f"0 ~ 100 = {sum_all(0,100)}")

def mul(*values):
    output = 1
    for value in values:
        output *= value
    return output

print(mul(5,7,9,10))

#
def factorial(n, front = True):
    result = 1
    if front:
        for i in range(1, n+1):
            if i != n:
                print(f"{i} x ",end="")
            else:
                print(f"{i} = ", end="")
            result *= i
    else:
        for i in range(n, 0, -1):
            if i != 1:
                print(f"{i} x ",end="")
            else:
                print(f"{i} = ", end="")
            result *= i
    return result


print(factorial(10,False))

# 도전 문제
# 3628800 숫자를 문자열로 변경한후.. 3자리마다 ,붙여서  아래와 같이 3,628,800 완성
# 1 x 2 x 3 x 4 x 5 x 6 x 7 x 8 x 9 x 10 = 3,628,800

