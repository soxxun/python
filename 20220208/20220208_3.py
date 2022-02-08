class Student:
    def __init__(self,name="" ,kor=0 ,eng=0 ,math=0 ,sience=0):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.sience = sience

    def getTotal(self):
        return self.kor+self.eng+ self.math + self.sience


s1 = Student("가나",90,95,99,100)
s2 = Student()
print(s1.name)
print(s1.getTotal())