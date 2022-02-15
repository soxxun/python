# 동명이인
# n명의 사람이름중에서 같은 이름을 찾아 집합으로 만들어 돌려주는 알고리즘
# ['tom','jerry','mike','tom']
#{ 'tom'}
# s = set()  # 중복을 허용하지 않고 순서가 없다
# s.add(1)
# s.add(2)
# s.add(2)
# s.add(3)
#
# s.discard(2)
# print(s)
#
# print(3 in s)

# 아래 로직의 문제점은 순환문을 다 돌지 않아도 중간에 이미 다 값을 찾은경우 나머지 순환문을
# 벗어날수 있도록 보완 할 것
name1 = ['Tom','Jerry','Mike','Tom']
name2 = ['Tom','Jerry','Mike','Tom','Mike','Tom','Jerry','Mike']
#name2에 있는 동명 이인
def find_same_name(names):
    result=set()
    for idx in range(len(names)):
        for nextidx in range(idx+1,len(names)):
            if(names[idx] == names[nextidx]):
                result.add(names[idx])
    return result

print(find_same_name(name1))
print(find_same_name(name2))
