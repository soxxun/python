# 클래스 비교연산
# 변수 비교연산

# 클래스도 하나의 변수 타입  ->  객체

# number1 = 10
# number2 = 20
#
# print(number1 == number2)
# print(number1 != number2)
# print(number1 > number2)
# print(number1 < number2)
# print(number1 >= number2)
# print(number1 <= number2)

class Student:
    def __init__(self,score,kor):
        self.score = score
        self.kor = kor
    def __eq__(self, other):
        return (self.score == other.getScore() and
                self.kor == other.getKor())
    def getScore(self):
        return self.score
    def getKor(self):
        return self.kor

s1 = Student(100,80)
s2 = Student(100,90)
print(f"s1==s2 : {s1 == s2}")
# print(f"s1 == s2 : {s1 == s2} {s1} {s2}")

# s3 = s4 = Student()
# print(f"s3 == s4 : {s3 == s4} {s3} {s4}")