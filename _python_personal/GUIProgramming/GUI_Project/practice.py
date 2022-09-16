
# zip
kor = ['사과', '바나나', '오렌지']
eng = ['apple', 'banana','orange']

zip(kor, eng) # 세로 방향으로 zip
print(list(zip(kor, eng)))

# unzip
# 1)
mixed = [('사과', 'apple'), ('바나나', 'banana'), ('오렌지', 'orange')]
print(list(zip(*mixed))) # 기호 '*'를 이용하여 각각 3개의 항목에 대해서 1번째끼리, 2번째끼리 다시 나누어 준 것

# 2)
kor2, eng2 = zip(*mixed)
print(kor2)
print(eng2)

