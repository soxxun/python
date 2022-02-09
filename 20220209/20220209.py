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
print(students[0])
print(students[0].values())
# print(sum(students[0].values()))
temp = students[0].values()
temp = list(temp)
temp2 = [i for i in students[0].values()]

sum = 0
for idx, value in enumerate(temp2):
    try:
        if idx != 1:
            sum += value
    except:
        pass
print(sum)




