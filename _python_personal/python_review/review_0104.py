
# 1 ~ 100까지 누적 합을 구하는 코드를 작성하세요.
'''
tot = 0

for i in range(100):
    i += i
print(i)
'''

# 다음 문자열 변수에서 공백을 제외한 문자의 수를 구하세요 (두 가지 방식)

# 1. 띄어쓰기를 제외한 글자수 세기
'''
st = "Python basic program language"
cnt = 0

for i in st:
    if i != " ":
        cnt += 1

print(cnt)
print(len(st)) # 띄어쓰기 포함 글자수

cnt = 0

for i in st:
    if i == " ":
        cnt -= 1
    cnt += 1
print(cnt)


# 2. 전체 글자수 - 띄어쓰기 글자수

cnt = st.__len__()

for i in range(0, len(st)):
    if st[i] == " ":
        cnt -= 1
print(cnt)
'''

# 1 ~ 30 까지 출력

#출력 형태
# 1	2	3	4	5	
# 6	7	8	9	10	
# 11	12	13	14	15	
# 16	17	18	19	20	
# 21	22	23	24	25	
# 26	27	28	29	30
'''
i = 0
# 1)
for i in range(1, 31):
    if i % 5 != 0:
        print(i, end = "\t")
    else:
      # print(i, end = "\n") - 디폴드값
        print(i)
    i += 1

# 2)
for i in range(1, 31):
    print(i, end="\t") 
    if i % 5 == 0:
        print() # 디폴드값 = "\n"
'''

# 모든 제어문은 중첩이 가능하다

# 다중 for문
# - for문 안에 for문이 있는 형태
# - 중첩적인 구조를 가지는 for문
'''
for i in range(1,4) : #외부 for문이 한 번 돌 때
    print("{}번째 외부 for문 실행".format(i))
    for j in range(1,4) : #내부 for문은 초기값부터 끝깞가지 반복됨
        print("내부 for문 실행")
    print("{}번째 외부 for문 종료".format(i))
'''
# i = 1로 한 번씩 돌 때 안의 j문은 (1, 4)니까 3번씩 처음부터 끝까지 반복
# 외부 3 * 내부 3라서 총 3번씩 총 9번이 돌게 됨



#구구단
# 2단 ~ 9단

#출력형태
#============2단=============
#2 * 1 = 2
#2 * 2 = 4
#2 * 3 = 6
#2 * 4 = 8
#2 * 5 = 10
#2 * 6 = 12
#2 * 7 = 14
#2 * 8 = 16
#2 * 9 = 18
#============================
#============3단=============
#3 * 1 = 3
#3 * 2 = 6
#3 * 3 = 9
#3 * 4 = 12
#3 * 5 = 15
#3 * 6 = 18
#3 * 7 = 21
#3 * 8 = 24
#3 * 9 = 27
#============================
# .........
'''
for i in range(2, 10): # 끝값은 미만이므로 +1 해 주어야 함
    print("="*8,f"{i}단","="*8)
    for j in range(1, 10):
        print(f"{i} X {j} = {i * j}")
    print("="*21)
'''
# 초기값 : 0 끝값 : 5 ( 미만 ) 증감값 : 1 ( 생략 가능 )
# 증감값이 (-)일 때는 끝값이 1 클때까지 반복 (초과)



# 1 ~ 30 까지 출력

# <출력 결과>
# 1   2   3   4   5
# 6   7   8   9   10
# 11   12   13   14   15
# 16   17   18   19   20
# 21   22   23   24   25
# 26   27   28   29   30

#다중for문이용

#외부for문 세로줄의 개수
#내부for문 가로줄의 개수

cnt = 0

for i in range(6):
    for j in range(5):
        cnt += 1
        print(cnt, end = "\t")
    print()


# 문제 1

'''
#
##
###
'''
a = "#"

for i in range(4):
    i *= a
    print(i)
print()


# 문제 2
'''
###
##
#
'''
for i in range(3, -1, -1):
    i *= a
    print(i)
print()


# 문제 3
'''
@##
@@#
@@@
'''
for i in range(3):
    for j in range(0, i+1, 1):
        print("@", end = "")
    for k in range(2, i, -1):
        print("#", end = "") # '\n'되지 않고 이어붙이기 위함
    print()

솔루션 SI

# 문제 4
'''
  #
 ###
#####
'''
n = 1
for i in range(3):
    for j in range(2, i, -1): # 2 초과이기 때문에 마지막 3번째에는 반복 X
        print(" ", end = "")
    for k in range(n):
        print("#", end = "")
    n += 2
    print()


