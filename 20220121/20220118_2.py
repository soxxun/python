ch01 = "안녕하세요"[0]
print(ch01)

#리터럴을 변경 할 수 없다
#"안녕하세요"[0] = "앙"

print("---------------------------")
print("안녕하세요")
print("안녕하세요"[1:4])
print("안녕하세요"[1:-1])
print("안녕하세요"[1:-2])
print("안녕하세요"[-1])
print("안녕하세요"[-2])

message = "안녕하세요"
train = message[0:-1]
test = message[-1]
print(train)
print(test)

print("안녕하세요"[0:])
print("안녕하세요"[0:10])
print("안녕하세요"[10])

# 슬라이싱은 indexError 없지만..
# 인덱스 방식은 over 하면 안된다
