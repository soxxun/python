# class 연습
# 만들기
# 사용하기

value = 100
def method():
    print(value)
method()

# 클래스 내부 변수를 만들때는 생성자에서 만들어 준다. - 기본적인 사용 방법  - 추천
# 클래스 맴버 변수는 생성자에서 초기화를 해주도록 ******
class TempClass:
    # innerValue = 0
    def __init__(self):
        self.innerValue = 0
    def innerMethod(self):
        print(f"innerMethod : {self.innerValue}")


a = TempClass()
a.innerValue = 100
print(a.innerValue)
a.innerMethod()