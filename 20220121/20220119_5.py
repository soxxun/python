#print("안녕하세요"[0])
#print("안녕하세요"[1])

# 5명의 학생의 점수를 관리...
# 개별변수
student1,student2,student3,student4,student5 = 80,98,88,99,97
# 리스트
students = [80, 98, 88, 99, 97, 88.5,"메롱"]  # 다른언어는 안그래요..... 같은 타입만
print(students)
students[0] = 100
print(students[0])
print(students[1:4])

#list_1 = [1,2]
#list_2 = [1,2]
list_1 = list_2 = [1,2]
print(list_1)
print(list_2)
print(list_1 == list_2)  # == 값을 비교
print(list_1 is list_2)  # is 메모리값을 비교
list_1[0] = 100


print(range(5))
for data in range(4,5):
    print(data)

# 1부터 10까지 합을 구해보세요..
#hint  +=
sum = 0;
for data in range(1,11):
    print(f"data = {data}")
    # code here

print(f"1~10까지의 합은 {sum}")