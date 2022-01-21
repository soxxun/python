list_a = [ 0, 1, 2, 3, 4, 5,30]
# list_a = 다른 어떤 함수의 결과로 계산된 리스트

# result = del list_a[0]  error del 명령어 방식
# result = list_a.pop(0)  ok  함수호출

# list_a.pop(인덱스)  --> 제거할 요소를 반환하고... 실제로도 제거하고
result = list_a.pop(0)
print(f"result = {result}")
print(f"list_a = {list_a}")

# 30이 리스트에 있으면 제거한다.
# if 조건문,bool변수 :
#   list_a.remove(30)
if 30 in list_a:
    list_a.remove(30)

list_a.reverse()
print(f"list_a = {list_a}")
list_a.reverse()
print(f"list_a = {list_a}")