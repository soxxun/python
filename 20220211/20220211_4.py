# 한줄씩 입력을 여러번 받아서
# 받을때마다 가장 작은수를 구하고
# 그 작은수 중에서 가장 큰수 찾기
# 하나의 for 문안에서 처리하기
# 각 입력단에서 가장 작은수 들 중에 큰수.... result
result = 0  # 작은 값들중에 가장 큰수
for i in range(5):
    num_list = list(map(int,input().split()))
    min_number =  min(num_list)
    if result  < min_number:
        result = min_number
# 결과 출력
print(result)

# 1 2 3 4       1
# 3 2 1 7       1
# 5 10 20 30    5
# 10 7 3 9      3
# 5 7 9 4       4
# result : 5