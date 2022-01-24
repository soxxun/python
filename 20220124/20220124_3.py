import random as rd
list_a = []
for i in range(10):
    list_a.append(rd.randrange(1,20))
print(list_a)

list_a_reverse = reversed(list_a)
# print(list_a_reverse)
print(list(list_a_reverse))

for i in list_a_reverse:
    print(i)

for i in reversed(list_a):  # 중간에 치환하지 않고 바로 reversed를 이용한다.
    print(i)

#     reversed를 이용해서 리스트를 뒤집으면 바로 사용할수 있는 상태가 아닌
#  상태를 가지는 객체로 변환되고
# 이때 이 객체를 for 문장에 넣으면 값을 가지고 온다.
# 그러나. list() 함수를 이용해서 reversed된 객체를 사용가능한 리스트로 변경하면  9번라인
# 더이상 for문에서 사용 할 수 없다

