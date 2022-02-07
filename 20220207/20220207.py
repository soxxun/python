# import math  # module import
# math.factorial()

# import math as m
# m.factorial()

# from math import factorial,floor,ceil
# factorial()

from math import factorial as fc
# fc()

from random import shuffle,seed,randrange
# seed(10)  # 파이썬만 그래요........ 다른 언어에서는 seed 값을 다이나믹하게 변경해 준다
temp = [1,2,3,4,5]
shuffle(temp)
print(f"temp={temp}")


# seed(randrange(0,100))
list_a =["a","b","c","d"]
print(f"shuffle(list_a) = {shuffle(list_a)}")
print(f"list_a = {list_a}")


