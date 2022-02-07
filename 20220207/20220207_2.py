# try ~ exception 적용해 보세요..
# Q1
result = []
for i in range(2000,3200+1):
    if(i % 7 == 0) and (i % 5 !=0):
        result.append(str(i))

result_str = ','.join( result)
print(type(result_str))
print(result_str)

# Q2
# for loop
x = 8
result = 1
for i in range(1,8+1):
    result *= i
print(f"{x} factorial = {result}")
# recursive Function
def myFactorial(x):
    if x == 1:
        return 1
    return x * myFactorial(x-1)
print(f"{x} factorial = {myFactorial(8)}")

#Q3
dic = {
    'a':10,'b':20
}
dic['c'] = 100
print(dic)

x = 5
# dic = dict()
dic = {}
for i in range(1,5+1):
    dic[i] = i**2
print(f"dic = {dic}")

#Q4
data = input(",를 기준으로 정수를 입력하세요")
data_split = data.split(',')
print(data_split)
print(tuple(data_split))

#Q5
# 사용자로부터 문자를 입력받는 함수
# 그 값을 출력하는 함수

def getString():
    return input("문자열을 입력하세요 : ")

def printString(data):
    print(data.upper())

#  사용
printString(getString())

# 클래스 규칙.... 대문자로 시작한다.
class InputOutputString():
    def __init__(self): #생성자
        print("생성자 호출")
        self.data

    def getString(self):
        self.data =  input("문자열을 입력하세요 : ")
    def printString(self):
        print(self.data.upper())

# InputOutputString클래스의 객체 생성
ob = InputOutputString()





