# 클래스 변수
# 인스턴스 변수
class Person:
    number = 0  # 클래스 변수
    def __init__(self):
        self.objnumber=0 #인스턴스 변수

# 클래스변수는  : 클래스명.클래스변수  객체.인스턴스변수 두개가 생긴다 초기화는 클래스변수의 값으로 된다
# 인스턴스 변수 : 객체.인스턴스변수

a = Person()
b = Person()
Person.number=100
Person.number=200
a.number = 0
Person.number=300

# Person.number = 300
print(f"Person.number : {Person.number}  a.number : {a.number} b.objnumber:{a.objnumber}" )
print(f"Person.number : {Person.number}  b.number : {b.number} b.objnumber:{b.objnumber}" )
