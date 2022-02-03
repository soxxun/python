# 7시 정각에 시작할께요..

#inputNum = 202202031256
# print(f"inputNum = {inputNum}")
# print(format(inputNum,','))

inputNum = input("정수를 입력하세요")
# 숫자를 뒤에서부터 3자리씩 끊어서 comma를 추가한다.
# print(list(reversed(inputNum)))
result = []
inputNum = list(reversed(inputNum))
for index,data in enumerate(inputNum):
    # print(f"{index} : {data}")
    if index % 3 == 0:
        result.append(',')
        result.append(data)
    else:
        result.append(data)

del result[0]
result = list(reversed(result))
result = "".join(result)
print(result)


