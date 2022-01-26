# 확인문제
key_list = ["name",'hp','mp','level']
value_list = ['기사',200,30,5]
character = {}

# character["name"] = '기사'
# character["hp"] = 200

for i in range(4):
    # print(f"kye={key_list[i]} value = {value_list[i]}")
    character[key_list[i]] = value_list[i]

print(f"character = {character}")

# 2번째 확인문제
limit = 10000
i = 0
sumValue = 0

while True:
    i += 1
    sumValue += i
    if(sumValue > limit):
        break

print(f"{i}을 더할때 {limit}를 넘으며 그때의 값은{sumValue} 입니다.")






