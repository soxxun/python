n = original = 1260
count = 0
# 화폐단위
coin_types = [500,100,50,10]
# 주어진 화폐단위로 거슬러 줄수 있는 동전의 개수
for coin in coin_types:
    count += + n // coin
    n %= coin
print(f"{original} 동전 총 갯수 : {count}")

# 500 으로 나누기
print(1260 // 500)
print((1260%500) // 100)
print( ((1260%500)%100) // 50 )
print( (((1260%500)%100)%50) // 10 )

