# 1. 랜덤하게 5개의 정수를 가지는 리스트를 만든다
# 2. 사용자로부터 정수를 입력받는다
# 3. 입력한 정수에 해당하는 리스트의 인덱스값을 출력한다.

import random
# 1. 전통적인 for
randomlist = []
for i in range(5):
    randomlist.append( random.randrange(0, 100) )

# 2. 리스트내포를 이용해 볼것  list comprehension
randomlist = [random.randrange(0, 100) for i in range(5)]

print(randomlist)
try:
    number = int(input("정수입력 : "))   # ValueError
    print(randomlist[number])   # IndexError
    randomlist[number] / number
except Exception as e:
    print(f"에러의 원인은 다음과 같습니다. {e}")
    print("적절한 해결책이 없습니다.")
except ValueError as e:
    print(f"에러의 원인은 다음과 같습니다. {e}")
    print("정수를 입력해 주세요")
except IndexError as e:
    print(f"에러의 원인은 다음과 같습니다. {e}")
    print(f"인덱스의 범위는 0 ~ {len(randomlist)-1}")






