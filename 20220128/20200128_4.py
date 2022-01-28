# 함수에서 외부의 변수를 참조

counter = 10

def getNames():
    global counter
    print(f"전역변수 :  {counter}")
    counter = 200


getNames()

print(f"전역변수 : {counter}")



# 함수외부의 변수는 global 변수이고
# 함수내부의 변수는 local 변수이다.  함수내부에서 global변수를 사용하려면 global 키워드를
# 변수앞에 붙여서 함수에서 외부변수를 사용한다는 의미

#튜플

a, b = [10,20]
print(f"a = {a}   b = {b}")
[a, b] = [10,20]
print(f"a = {a}   b = {b}")
a, b = (10,20)
print(f"a = {a}   b = {b}")
(a, b) = (10,20)
print(f"a = {a}   b = {b}")

tuple_test = 10,20,30,40
print(f"tuple_test = {tuple_test}")
# tuple_test[0] = 100  # error

a,b,c = 10,20,30
a = 100
print(f"a:{a}")
a,b,c = (10,20,30)
a = 100
print(f"a:{a}")
a,b,c = [10,20,30]
a = 100
print(f"a:{a}")







