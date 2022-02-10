# 클래스 변수 / 함수  -->  클래스명.0000   : 공통
# 인스턴스 변수/ 함수 --> 객체.000   : 독립

class Car:
    serialNumber = 0
    def __init__(self):  # self 객체
        Car.serialNumber += 1
        self.sc = Car.serialNumber
    @classmethod
    def classMethod(cls):   # 클래스메소드는 인스턴스 변수를 사용 할수 없다  cls : 클래스
       print(f"class method call {cls.serialNumber}")

    def nomalMethod(self):
        print(f"nomalMethod call {Car.serialNumber}  {self.sc}")

Car.cnumber = 200
Car.classMethod()
(Car()).nomalMethod()

a = Car()
b = Car()
c = Car()
print(f"a serialNumber : {a.sc}")
print(f"a serialNumber : {b.sc}")
print(f"a serialNumber : {c.sc}")


