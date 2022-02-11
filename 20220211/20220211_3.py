# set의 자료구조
# 중복을 허용하지 않는다  key의 속성을 갖는다
# 순서를 보장하지 않는다
# 리스트의 중복을 제거하는 용도로 사용 많이....... set(리스트)   ->   그결과에 list() 씌워준다
list_a =[3,3,3,1,1,2,1,1,2,2,3,2,3,3]
# list_a = set(list_a)  # 리스트를 -> set 변환 : 이유는 중복제거
# print(list_a)
# list_a = list(list_a) # set --> list로 원복 :타입을 원복
list_a = list(set(list_a))

set_a = set([1,2,2,3,4,1,2])
# print(set_a[0])   # 에러...
# set은 인덕스형태로 각각의 요소에 접근 못한다... 그럼 어떻게?
# 리스트나 튜플로 변경해서 사용
set_a = tuple(set_a)
print(set_a[0])

# A [1,2,3,4,5]
# B [3,4,5,6,7]
A = set([1,2,3,4,5])
B = set([3,4,5,6,7])
print(A & B)
print(A.intersection(B))

print(A | B)
print(A.union(B))

print(A - B)
print(A.difference (B))

inter = []
for i in [1,2,3,4,5]:
    for j in [3,4,5,6,7]:
        if i == j:
            inter.append(i)

