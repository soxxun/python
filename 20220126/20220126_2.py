# reversed는 재사용 금지
temp = reversed([1,2,3,4,5,6])

print(list(temp))
# reversed(temp)
print(list(temp))

print("첫번째 for loop")
for i in reversed([1,2,3,4,5,6]):
    print(i)

print("두번째 for loop")
for i in reversed([1,2,3,4,5,6]):
    print(i)

print(list(temp))


# dictionary items()  enumerate()

dic_1 = {
    "a": 1, "b": 2, "c": 3, "d": 4
}
print(f"dic_1.items() = {dic_1.items()}")
print(f"list(dic_1) = {list(dic_1)}")
print(f"dic_1.keys() = {dic_1.keys()}")
print(f"list(dic_1.keys()) = {list(dic_1.keys())}")
print(f"dic_1.values() = {dic_1.values()}")
print(f"list(dic_1.values()) = {list(dic_1.values())}")

for key, value in dic_1.items():
    print(f"key:{key}  value:{value}")

#리스트 내포