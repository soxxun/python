# 제너레이터
# list_a = [10,20,50,30]
# print(list_a)
# print(reversed(list_a))

def test():
    print("test 함수 호출1")
    yield 1
    print("test 함수 호출2")
    yield 2
    print("test 함수 호출3")
    yield 3

print(test())
print("---------------------")

output = test()

for i in test():
    print(i)

result = next(output)
print(f"result = {result}")
result = next(output)
print(f"result = {result}")
result = next(output)
print(f"result = {result}")
# error
result = next(output)
print(f"result = {result}")

