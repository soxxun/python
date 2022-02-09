# __str__()
class Student:
    def __init__(self,name,score):
        self.name = name
        self.score = score
    def __str__(self):          # 클래스 내부 변수의 값을들 출력할때 사용
        return f"name:{self.name}\tscore:{self.score}"
# 클래스 외부
s = Student("홍길동", 98)
list_a = [Student("홍길동", 98),Student("철이", 95),Student("미애", 91)]
for i in list_a:
    print(i)


