print(range(100))
print( list(range(100)) )

# 1부터 15까지의 연속된 숫자로된 리스트를 가지고 싶다.
list_a =  list(range(1,16))
print(f"list_a = {list_a}")

for i in range(5):
    print(f"i = {i}")

print()
for i in [0,1,2,3,4]:
    print(f"i = {i}")


# 구구단....
# 3 x 1 = 3
# 3 x 2 = 6


# 3 x 9 = 27

#print("3 x 1 = 3*1")
#print("3 x 2 = 3*2")
#print("3 x 3 = 3*3")
#print("3 x 4 = 3*4")
# ...
#print("3 x 9 = 3*9")
data = 200
print(f"data = {data}")
# 순환문... for문의 특징....... 반복.... 지정된 횟수가 반드시 존재함
for data in range(1,10):  # 1 2 3 4 5 6 7 8 9
    print(f"3 x {data} = {3 * data}")

print(f"data = {data}")

list_a = list(range(8))
print(f"list_a = {list_a}")
list_a.extend(list_a)
print(f"list_a = {list_a}")
list_a.append(10)
print(f"list_a = {list_a}")
list_a.insert(3,0)
print(f"list_a = {list_a}")
list_a.remove(3)
print(f"list_a = {list_a}")
list_a.pop(3)
print(f"list_a = {list_a}")
list_a.clear()
print(f"list_a = {list_a}")