# class 생성
# 클래스명은 항상 첫글자가 대문자.... 문법X 개발자사이의 암묵적인 약속
def F():
    pass

# 1.생성
class Student:
    # 생성자(함수)
    def __init__(self):  #생성자 함수
        print("생성자 호출")
    number = 0
    def A(self):
        print("A")
    def B(self):
        print("B")
    def C(self):
        print("C")

# 2.객체(변수)
print("s 객체생성전")
s = Student()  # 객체를 생성하기위해 생성자 호출   객체 2를 생성
print("s 객체생성후")
print("s2 객체생성전")
s2 = Student()
print("s2 객체생성후")

# 3.객체를 통해 사용
s.A()
s.B()
s.C()
s.number =20
print(s2.number)
