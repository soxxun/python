#기본매개변수는 맨 마지막 부터 사용한다.
# 기본매개변수는 생략 가능하다.
def Test(a = 0, b = 0, c = 0):
    print(f"{a}  {b}  {c}")

Test(10)
Test(10, 20)
Test(10, 20, 30)

Test(10)
Test(c= 10, b = 20)
Test(10, 20, 30)

# def Test2(n=2 *values):
#     print(f"n={n} *values={values} ")
#     pass

# Test2(1,2,3,4,1,5,4,1,5,1)


def Test3(*values, n=0):
    print(f"n={n} *values={values} ")
    pass

Test3(1,2,3,4,1,5,4,1,5,100)
Test3('abc','bcd',100)


for i in range(100):
    print('.',end="")