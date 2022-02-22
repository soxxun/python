import numpy as np
test_array = np.arange(1,13).reshape(3,-1)
third_order_tensor =  np.array([test_array,test_array,test_array])
print(third_order_tensor)

# print( third_order_tensor.sum(axis=0))
print( third_order_tensor.sum(axis=2))

# std 표준편차
test_array.std()
# 제곱근근np.sqrt(test_array)

#내적연산
print("----------------------------------")
x_1 = np.arange(1,7).reshape(2,-1)
x_2 = np.arange(1,7).reshape(3,-1)
print(x_1)
print(x_2)
#print(x_1.dot(x_2))
print(x_2.dot(x_1))

#브로드 캐스팅
x = np.arange(1,10).reshape(3,3)
print(x+10)
print(x-2)
print(x//3)
print(x**2)