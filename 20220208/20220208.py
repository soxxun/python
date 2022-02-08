import random as rd
namelist = "가나다라마바사아자차카타파하"
students = []
for i in range(10):
    d = dict()
    d["name"] = rd.choice(namelist) + rd.choice(namelist)
    d["korean"] = rd.randrange(40,100)
    d["math"] = rd.randrange(40,100)
    d["english"] = rd.randrange(40,100)
    d["science"] = rd.randrange(40,100)
    students.append(d)

print("이름","총점","평균",sep = "\t")
print("------------------------------")
for student in students:
    name = student["name"]
    total = student['korean']+student['math']+student['english']+student['science']
    avg = total / 4
    print(name, total, avg, sep="\t")


