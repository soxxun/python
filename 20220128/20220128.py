# 함수의 매개변수
def Test(a, b):
    pass

Test(10, 20)
# -----------------------------------------
def Test2(a, b = 0):
    pass

Test2(10)
Test2(10, 20)
# -----------------------------------------

def Test3(*a):
    pass

Test3(1)
Test3(1,2)
Test3(1,2,3)
# -----------------------------------------
def Test4(a, *b):
    print(f"(a, *b) a = {a}, *b={b}")
Test4(1,2,3)  # a = 1  b = [2,3]

def Test5(a = 100, *b):
    print(f"(a = 100, *b) a = {a}, *b={b}")
Test5(1,2,3) # a = 1 b = [2, 3]

# Error
# def Test6(*b, a):
#     print(f"(*b, a) a = {a}, *b={b}")
# Test6(1,2,3)

def Test7(*b, a = 100):
    print(f"(*b, a = 100) a = {a}, *b={b}")
Test7(1,2,3) # b = [1, 2, 3] a = 100

