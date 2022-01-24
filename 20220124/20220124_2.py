for i in range(10):
    print(f"{i}번째 반복입니다.")  # 비지니스로직


i = 0
while i< 10:
    print(f"{i}번째 반복입니다.")
    i += 1

list = [1,2,4,5,1,4,2,2]
list.remove(2)

temp = []
for i in list:
    if i != 2:
        temp.append(i)

print(temp)
list = temp
print(list)

list = [1,2,4,5,1,4,2,2]
v = 2
while v in list:
    list.remove(v)





