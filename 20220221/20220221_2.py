import numpy as np
test_ary = np.array([1,2,3,4])
print(test_ary)
print(type(test_ary))
test = [1,2,3,4]
print(test)
print(type(test))

test = [
    [1,2,3,4],
    [5,6,7,8]
]
print(test[0][0])

print(np.array(test))
print( (np.array(test))[0][0] )

# 배열..... 배열 : 연속적인 데이터생성, 동일한 데이터만 저장가능
list_test = [1,2,"10",3]
# list_test = [1,2,10.25,3]
print(f"파이썬 리스트 : {list_test}")
print(f"np.array(list_test) : {np.array(list_test)}")
print(f"np.array(list_test,float) : {np.array(list_test,float)}")

#넘파이 배열의 구성은 tuple
temp = np.array(list_test)
print(temp.shape)
temp2 = np.array(
    [
        [1,2,3],
        [3,4,5],
        [3,4,5],
        [3,4,5]
]
)
print(temp2.shape)
print(temp2.size)

# dtype
temp = np.array([[1,2,3],[4,5,6]],dtype = np.int64)
temp = np.array([[1,2,3],[4,5,6]],int)

print(f"temp shape : {temp.shape}")
temp = temp.reshape(-1)
print(temp)
print(temp.shape)



