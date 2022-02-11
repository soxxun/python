# coding test
# 숫자 3개를  공백을 기준으로 입력받기
# a,b,c = list(map(int ,input("숫자를 공백을 기준으로 3개 입력하세요").split()))

# N개의 숫자를 공백을 기준으로 입력받기
# 그  숫자들 중에서 가장 큰수와 두번째로 큰수를 출력
# 중복 값이 존재할 수도 있음

N = list(map(int,input("숫자를 공백기준으로 입력하세요").split()))
N.sort(reverse=True)

# rank를 응용  10 50 20 30 50 50 30
# [50, 50, 50, 30, 30, 20, 10]
print(N)
set_n = set(N)
print(f"set_n의 자료형은 {type(set_n)}")
set_n = list(set_n)
set_n.sort(reverse=True)
N = set_n
print(N)
print(f"가장큰수:{N[0]}  두번째 큰수:{N[1]}")
# first = N[0]
# second = 0
# for i in N:
#     if first != i:
#         second = i
#         break
# print(f"가장큰수:{first}  두번째 큰수:{second}")
