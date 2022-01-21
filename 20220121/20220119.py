original_money = money = int(input("교환할 돈:"))

# Q1 money의 데이터 타입은 ?
print(f"입력한 돈은 {money}원 입니다.")
print(f"입력받는 money의 타입은 {type(money) } 입니다.")

money_500, money_100, money_50, money_10 = 0, 0, 0, 0

money_500 = money // 500
money %= 500  # money = money % 500

money_100 = money // 100
money %= 100

money_50 = money // 50
money %= 50

money_10 = money // 10
money %= 10

print(f"입력한 {original_money}의 거스름돈은 500:{money_500}, 100:{money_100},"
      f"50:{money_50}, 10:{money_10}, {money}")