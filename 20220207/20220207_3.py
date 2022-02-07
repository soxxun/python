# 클래스 규칙.... 대문자로 시작한다.
class InputOutputString():
    def __init__(self):  # 생성자
        print("생성자 호출")
        self.data = ""

    def getString(self):
        self.data = input("문자열을 입력하세요 : ")

    def printString(self):
        print(self.data.upper())

# InputOutputString클래스의 객체 생성
ob = InputOutputString()
ob.getString()
ob.printString()