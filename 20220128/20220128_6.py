def call10Times(func):
    for i in range(10):
        func()

def callFunction(func):
    return func(5)


#불필요함...
def fa(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

print(callFunction(fa))
# def show():
#     print("hello")
# call10Times(show)

call10Times(lambda : print("hello"))

