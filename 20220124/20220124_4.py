list_a = ['a','b','c','d']

count = 0
for i in list_a:
    print(f"{count}번째 요소는 {i} 입니다.")
    count += 1

print()

for i in range(len(list_a)):
    print(f"{i}번째 요소는 {list_a[i]} 입니다.")

print()

# print(f"enumerate(list_a) = {enumerate(list_a)}")
# print(f"list(enumerate(list_a)) = {list(enumerate(list_a))}")
# for i, value in enumerate(list_a):
#     print(f"{i}번째 요소는 {value} 입니다.")

# 20220124_3번 파일의 reversed 처럼 객체로 변환된 값을 list로 변경하면 그 객체는
# 더이상 집합의 상태를 가지지 않는다. 그래서 25번 라인이 실행 안된다.
changed = enumerate(list_a)
print(changed)
print(list(changed))
for i, value in changed:
    print(f"{i}번째 요소는 {value} 입니다.")

