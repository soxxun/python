# 함수의 매개변수로 함수를 전달할때
# 전달할 함수가 미리 정의되어 있어야 한다

test = [1, 2, 3, 4, 5]
print(test[::-1])
print(list(reversed(test)))



#main function
def call_2_times(f):
    for i in range(2):
        f()

# sub function
# def f1():
#     print("a")
#
# def f2():
#     print('b')

# real use
# 람다는 익명의 함수(이름없이 사용하는 함수)
call_2_times(lambda : print('a'))
call_2_times(lambda : print('b'))

def power(item):
    return item*item
def under_3(item):
    return item < 3

list_input_a = [5,3,8,2,1,5]
# [1,4,9,16,25]
result = []
for data in list_input_a:
    result.append(power(data))
print(f"result = {result}")

result = []
for data in list_input_a:
    if under_3(data):
        result.append(data)
print(f"result = {result}")


result = map(power,  list_input_a)
print(f"result = {list(result)}")

result = filter(under_3, list_input_a)
print(f"result = {list(result)}")

# 람다를 이용해서 위의 식을 변경하기
result = map(lambda x: x * x ,  list_input_a)
print(f"lambda result = {list(result)}")

result = filter(lambda x: 0 < x < 10, list_input_a)
print(f"lambda result = {list(result)}")


