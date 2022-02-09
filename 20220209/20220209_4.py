class Student:
    def doWorkStudy(self):
        print("공부합니다.")

class Teacher:
    def doWorkTeach(self):
        print("가르칩니다.")

# s --> 객체
# Student() -->   매개변수가 없는 생성자 호출

list_a = [Student(), Teacher(), Student(), Student(), Teacher()]
for obj in list_a:
    if isinstance(obj, Student):
        obj.doWorkStudy()
    elif isinstance(obj, Teacher):
        obj.doWorkTeach()
    else:
        pass


