students = []
student1 = {
    "id" : 1,
    "name" :"홍길동",
    "kor" : 80,
    "eng" : 87,
    "math" : 88,
    "rank" : "A"
}
student2 = {}
student2["id"],student2["name"],student2["kor"] = 2,"이순신",80
student2["eng"],student2["math"],student2["rank"]  = 88,98,"B"

students.append(student1)
students.append(student2)

students.append({
    "id" : 3,
    "name" :"강감찬",
    "kor" : 80,
    "eng" : 87,
    "math" : 88,
    "rank" : "C"
})
print(len(students))

# 리스트내의 모든 요소(딕션너리)를 출력
for d in students:
    print(d)

# 학생들중에 학점이 C가 아닌  학생의 이름을 출력해라.
for s in students:
    if s['rank'] != 'C':
        print(s["name"])



