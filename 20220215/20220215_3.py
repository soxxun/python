# [17, 92, 19, 33, 58, 5, 33, 42]
# (19,33,900)값을 리스트에 찾아서 위치를 돌려주는 프로그램
lists = [17, 92, 19, 33, 58, 5, 33, 42,5]

def findIndex(number,lists):
    for i in range(len(lists)):
        if(number == lists[i]):
            return i
    return -1

result = []
for i in [19,33,900]:
    result.append(findIndex(i,lists))

# for i in [19,33,900]:
#     count = 0
#     isNotFind = True
#     for j in range(len(lists)):
#         if(i == lists[j]):
#             result.append(count)
#             isNotFind = False
#             break
#         count += 1
#     if isNotFind:
#         result.append(-1)
print(result)
# [2,3,-1]

# 정렬
# lists.sort()  #이것을 구현
print(lists)
result.clear() # 초기화

while(len(lists)>0):
    min_lists = min(lists)
    lists.remove(min_lists)
    result.append(min_lists)
print(f"result = {result}")

# #1
# min_lists = min(lists) # 최소값을 구하고
# result.append(min_lists) # 결과에 추가
#
# #2
# lists.remove(min_lists) # 기존 리스트에서 이미 구한 최소값을 제거
# min_lists = min(lists) # 최소값 구하고
# result.append(min_lists) # 결과에 추가
#
# #3
# lists.remove(min_lists)
# min_lists = min(lists)
# result.append(min_lists)



# [5, 17, 19, 33, 33, 42, 58, 92]

