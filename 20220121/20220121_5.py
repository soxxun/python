numbers = [1,1,4,5,2,1,4,1,5,8,4,7,4,8,5,1,4,1,5,4,1,2,3,6,5,8,9,8,7,4,5,1,4,5]
counts = { }

for num in numbers:
    # if num not in counts:
    if counts.get(num) == None:
        counts[num] = 0
    #counts[num] = counts[num] + 1
    counts[num] += 1

print(counts)

# 도전문제..
# 가장 많이 나온수는 ??


# hint
# counts[1] = 0
# counts[1] = counts[1]+1
# counts[1] = counts[1]+1

# counts[2] = 0
# counts[2] = counts[2]+1
# counts[2] = counts[2]+1
# counts[2] = counts[2]+1

# print(counts)