# extend()  새로운 리스트의 모든 요소를 추가   ( 리스트  )
# append()  새로운 요소    ( 요소 )
# 요소(element)  리스트를 구성하는 값

list_a = [1, 2, 3]
list_b = [10, 11, 12, [50, 60] ]

list_a.extend(list_b)  # 리스트  + 리스트
print(f"list_a.extend(list_b) = {list_a}")

list_a.append(list_b)
print(f"list_a.append(list_b) = {list_a}")
