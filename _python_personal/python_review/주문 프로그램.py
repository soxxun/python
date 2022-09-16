
menu = ("짜장면", "짬뽕")
pay = 0

for jajang, jambbong in menu:
    a = 5000
    b = 6000
    order = input("메뉴 입력 : ")
    if order == jajang:
        a += a
        su = int(input("수량 : "))
        if su >= 5:
            a -= 3000
        elif su >= 10:
            a *= 0.1
        else:
            a *= su

    elif order == jambbong:
        b += b
        su = int(input("수량 : "))
        if su >= 5:
            b -= 3000
        elif su >= 10:
            b *= 0.1
        else:
            b *= su
    else:
        print("메뉴를 정확히 입력해 주세요.")
        
    print(f"총 금액은 {jajang + jambbong:,d}원입니다.")


# =========================================================================


menu = [['칼국수', 6000],
        ['비빔밥', 5500],
        ['돼지국밥', 7000],
        ['돈까스', 7000],
        ['김밥', 2000],
        ['라면', 2500]]

check = True

menu = []
food = input("메뉴 입력 : ")
price = int(input("가격 입력 : "))

for i in menu:
    if i[0] == name:
        i[1] = price
        check = False
        break

    IsContinue = input("이어서 추가하시겠습니까?(Y/N) : ")
    if IsContinue.upper == "y":
        return
    else:
        pass
if check:
    menu.append([food, price])
    
print(menu)


# =========================================================================

# dictionary

# 사용자 입력으로 메뉴와 가격을 입력 받아 menu 변수에 자료를 추가
menu = {}

for i in range(2):
    
    user = input("메뉴 입력 : ")
    price = int(input("가격 입력 : "))
    
    if user != i:
        menu.update({user : price})
    if user == i:
        menu[i] = price
    isContinue = input("이어서 추가하시겠습니까? (Y/N) : ")
    if isContinue.upper == "n":
        break
    elif isContinue.upper == "y":
        i += 1
        continue
    else:
        print("영문자를 정확히 입력해 주시길 바랍니다.")
    i += 1
print(menu)
