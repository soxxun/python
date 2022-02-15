#딕셔너리를 이용한 동명이인
d = {"Summer":100,"Winter":200}
d["Summer"] = 200
print(d)
# name2 = ['Tom','Jerry','Mike','Tom','Mike','Tom','Jerry','Mike']
# name_dict = {
#     'Tom' : 3,
#     'Jerry' : 2,
#     'Mike' : 2
# }
# 1.각 이름이 등장하는 횟수를 저장할 빈 딕셔너리(name_dict)를 만듦
# 2.입력으로 주어진 리스트에서 각 이름을 꺼내면서 반복
# 3.주어진 이름이 name_dict에 있는지 확인
# 4.이미 있다면 등장 횟수를 1 증가시킴
# 5.아직 없다면 그 이름을 키(key)로 하는 항목을 새로 만들어 1을 저장
# 6. 1~5번 과정을 거치면 name_dict에는 리스트에 등장하는 모든 이름과 각각의 등장 횟수가 저장됨
# 7.만들어진 딕셔너리에서 등장 횟수가 2 이상인 이름을 찾아 결과 집합에 넣은 다음 출력으로 돌려줌
names = ['Tom','Lee','Jerry','Mike','Tom','Mike','Tom','Jerry','Mike']
name_dic = {}
for name in names:
    if name in name_dic:
        name_dic[name] += 1
    else:
        name_dic[name] = 1
print(name_dic)









