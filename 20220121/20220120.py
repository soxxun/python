list_a = [1,2,3]
list_a.append(4)
print(list_a)

# print(list_a + 5) error list +연산은 list끼리
print(list_a + [5])  # append 효과
#list_a = list_a + [5]
list_a += [5]
print(list_a)
a = 10
#a = a +20
a += 20

# append 동급연산
# list += [요소]


list_a.insert(0,100)
print(list_a)

list_a =  list_a.insert(0,100)
print(list_a)

# 사용자로부터 from to 를 받아서 그 사이의 값들의 합을 출력

# 개선점.... 작은거 ~ 큰거
num1 = int(input("첫번째 숫자:"))
num2 = int(input("두번째 숫자:"))
# 조건  num1 과 num2의 크기를 비교해서  num1 > num2
# --> 두 변수값을(swap) 치환

sum = 0
for data in range(num1,num2+1):
    sum += data;
print(f"{num1} ~ {num2} 까지의 합은 {sum}입니다.")



