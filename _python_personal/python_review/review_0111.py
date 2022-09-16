
# Day09 - Dictionary
'''
dic = {"숫자" : 0, "실수" : 1.1, "과일" : ["포토","딸기"]}

print(dic)
print(type(dic))
print(dic["숫자"]) #대괄호 안의 값이 key값

#key값을 통해 value값을 찾는다고 해서 dictionary라고 정의된 것

print(dic["실수"])
print(dic["과일"][0]) #포도
print(dic["과일"][1]) #딸기
print()

for key in dic :
    print(f"{key}, {dic[key]}")
print()

#독특한 점
#   key : 인덱스 전체를 뽑아오는 것이 아니라 dic 안에 있는 key만 뽑아 옴
#   - dic의 key값만 변수에 담긴다
#   - key = "숫자" key = "실수" key = "과일"


dd = { "park" : {"age" : 25, "blood" : "B"},
       "kim" : {"age" : 37, "blood" : "A"} }

print(dd["park"])
print(dd["park"]["age"]) # dd[큰틀의 키값][작은틀의 키값]
print()


for name in dd: #name = "park" / name  "kim"
    for key in dd[name]: #dd["park"] -> key = "age" / key = "blood"
                         #dd["kim"] -> key = "age" / key = "blood"
        print(dd[name][key])
        
# name : 큰 틀의 키 값
# key : 작은 틀의 키 값




# 인덱스로 묶어줄 경우

ld = [ {"name" : "Park", "age" :  25, "blood" : "B"},
       {"name" : "kim", "age" : 37, "blood" : "A"} ]

print(ld[0]["name"]) # Park
print()



#반복문 - 전체 key : value 출력 시

for i in ld :
    for key in i : # i = {"name" : "Park" , "age" : 25 , "blood" :"B"}
                   # i = {"name" : "Kim" , "age" : 37 , "blood" : "A"}
                   
        print("{} : {}".format(key,i[key]))
print()
'''

# =======================================================================

'''
dic = {"a" : 1, "b" : 2, "c" : 3}

#Dictionary(사전형)에서 사용되는 함수

# update(dic)
# - 사전형 자료에 값을 추가
# - key값이 같으면 value값만 바꾸고 key값이 없으면 추가시킴
dic.update({"a" : 4})
print(dic)
print()

dic.update({"d" : 5})
print(dic)
print()

# fromkeys(iter,value)
# - 리스트, 튜플에 존재하는 값을 키로 사전형 자료를 생성하여 반환
# - value값은 '일괄적'으로 설정될 수밖에 없음
ls = [1,2,3,4]
print(ls)
print(dic.fromkeys(ls,1)) #전부 1로 변경 (value값은 하나만)
print()

# get(key,[value])
# - 사전형의 키를 통하여 값을 반환
# - 키값이 없으면 None을 반환 (None - 아무 값도 없음을 의미)
# - 키값이 있으면 value값을 반환
# - 키값이 없어도 value값을 설정하면 value값을 반환
print(dic.get("a")) # == dic["a"]
print(dic.get("e"))
print(dic.get("e",1)) #임시로 1을 value값으로 설정하여 1을 출력
print()

# keys()
# - 사전형의 모든 키를 반환
# - 리스트나 튜플 타입으로 변환하여 사용 가능
key = dic.keys()
print(key)

key = list(key)
print(key)
for i in key:
    print(i)
print()

# values()
# - 사전형의 모든 값 반환
# - 리스트와 튜플타입으로 변환하여 사용 가능
# - 사전형의 모토가 벗어나므로(키값 사라짐) 잘 사용되지 않음
print(tuple(dic.values()))

# items()
# - 사전형의 모든 key - value를 쌍으로 '튜플'로 반환
# - 리스트나 튜플타입으로 변환하여 사용 가능
tp = dic.items()
print(tp)

# pop(key)
# - 사전형의 키를 통해 value값을 반환 후 '삭제'
# - key값이 없으면 error
print(dic.pop("a"))
print(dic)

# popitem()
# - 사전형의 key - value의 쌍을 '튜플로 반환 후 삭제'
# - 맨뒤에 있는 데이터부터 삭제
print(dic.popitem())
print(dic)

# clear()
# - 사전형의 모든 key - value를 삭제하여 빈 사전형 자료만 남음
dic.clear()
print(dic)
'''
# =======================================================================

# 다음의 메뉴와 가격을 Key와 Value로 사용하여 사전형 자료를 
# 만드시오. (변수명은 menu)
# 칼국수(6000원), 비빔밥(5500원), 돼지국밥(7000원), 
# 돈까스(7000원), 김밥(2000원), 라면(2500원)
'''
menu = {
    "칼국수" : 6000,
    "비빔밥":5500,
    "돼지국밥" : 7000,
    "돈까스" : 7000,
    "김밥" : 2000,
    "라면" : 2500
    }


# 가격이 6000원 미만에 해당하는 메뉴와 가격을 출력하는 코드를 작성하시오.
for i in menu: # menu의 키값만 뽑아옴
    if menu[i] < 6000: #키값의 value 뽑아옴
        print(f"{i} : {menu[i]}원")



# 사용자 입력으로 메뉴와 가격을 입력 받아 menu 변수에 자료를 
# 추가 할 수 있도록 하시오. (동일한 메뉴는 가격만 변경)

user = input("메뉴 입력 :")
price = int(input("가격 입력 :"))
menu.update({user : price})
print(menu)



# 메뉴를 자동으로 선택하여 출력하는 코드를 작성 하시오
import random as rd
keys = list(menu.keys())
# print(keys)
rand = int(rd.random() * len(keys))
print(f"오늘의 랜덤 메뉴는 '{keys[rand]} : {menu[keys[rand]]}'입니다.")
'''

# Day09 - Test05
# 가수 이름, 구성원 수 입력 받고 출력까지 할 수 있는 코딩
# (5명만 입력하고 출력하세요)
# 단, 가수 이름 겹치지 않게


# while문
'''
dic = {}

while len(dic) < 3:
    name = input("가수 이름 :")
    su = int(input("구성원 수 :"))

    if dic.get(name) == None: # dic.get(key) -> key값이 없으면 None,
                              # 있으면 value값 반환하는 함수
        dic.update({name : su})
        print("데이터가 추가되었습니다")
    else:
        print("데이터가 이미 존재합니다")

for key in dic:
    print("{} : {}".format(key,dic[key]))


# for문
# incomplete *** (continue 안 먹음)

dic = {}

for i in range(3):
    
    name = input("가수 이름 입력 : ")
    su = int(input("구성원 수 입력 : "))

    if name in dic.keys():
        print("가수명이 중복됩니다. 다시 입력해 주세요")
        i -= 1
        continue

    elif name not in dic.keys():
        dic.update({name : su})
        print("성공적으로 추가되었습니다 !")
   
print(dic)
'''
# =======================================================================

# 학생의 인적 사항 등록 후 검색 프로그램
# - 학번 , 이름 , 주소 

# { 학번 : { name : 이름 , addr : 주소 } }

# 1. 인적사항 등록
# 2. 검색 - 학번 검색
# 3. 수정
# 4. 삭제
# 5. 전체 보기
# 6. 종료

#info = { 학번 : { 'name' : 이름 , 'addr' : 주소 } ,
#         학번 : { 'name' : 이름 , 'addr' : 주소 } }

"""
info = {}

while True:
    print('''
1. 인적사항 등록
2. 검색 - 학번검색
3. 수정
4. 삭제
5. 전체보기
6. 종료''')

    select = int(input("번호 입력 : "))
    if select == 1:
        hacbun = int(input("학번 입력 : "))
        if info.get(hacbun) == None:
            name = input("이름 입력 : ")
            addr = input("주소 입력 : ")
            one = { hacbun : {'name' : name, 'addr' : addr }}
            info.update(one)
            print(f"{name}님의 학적정보 추가 완료")

    elif select == 2:
        hacbun = int(input("학번 입력 : "))
        one = info.get(hacbun)
        if one == None:
            print("존재하지 않는 학번입니다.")
        else:
            print(f"{'='*20}\n"
                  f"학번 : {hacbun}\n"
                  f"이름 : {one['name']}\n"
                  f"주소 : {one['addr']}\n"
                  f"{'='*20}")

    elif select == 3:
        hacbun = int(input("학번 입력 : "))
        one = info.get(hacbun)
        if one == None:    
            name = input("이름 입력 : ")
            addr = input("주소 입력 : ")
            one['name'] = name
            one['addr'] = addr
          # info.update({no : { 'name' : name , 'addr' : addr }}) 이렇게도 가능
            print("변경 완료!")
                    
    elif select == 4:
        hacbun = int(input("학번 입력 : "))
        one = info.get(hacbun)
        if one == None:
            print("존재하지 않는 학번입니다.")
        else:
            name = input("이름 입력 : ")
            if one['name'] == name:
                info.pop(hacbon)
                print(f"{name}님의 정보 삭제 완료")
            else:
                print("이름을 잘못 입력하셨습니다.")

    elif select == 5:
        for hacbun in info:
            one  = info.get(hacbun)
            print(f"{'='*20}\n"
                  f"학번 : {hacbun}\n"
                  f"이름 : {one['name']}\n"
                  f"주소 : {one['addr']}\n"
                  f"{'='*20}")

    elif select == 6:
        break
    else:
        print("번호를 잘못 입력하셨습니다.")
"""

# 오류 발생 시
"""
info = {}

while True:
    print('''
1. 인적사항 등록
2. 검색 - 학번검색
3. 수정
4. 삭제
5. 전체보기
6. 종료''')
    try:
        select = int(input("번호 입력 : "))
    except:
        print("*** 입력 오류 ***")
        continue
    if select == 1:
        try:
            hacbun = int(input("학번 입력 : "))
            if info.get(hacbun) == None:
                name = input("이름 입력 : ")
                addr = input("주소 입력 : ")
                one = { hacbun : {'name' : name, 'addr' : addr }}
                info.update(one)
                print(f"{name}님의 학적정보 추가 완료")
        except:
            print("*** 입력 오류 ***")
            continue

    elif select == 2:
        try:
            hacbun = int(input("학번 입력 : "))
            one = info.get(hacbun)
            if one == None:
                print("존재하지 않는 학번입니다.")
            else:
        print("번호를 잘못 입력하셨습니다.")                print(f"{'='*20}\n"
                      f"학번 : {hacbun}\n"
                      f"이름 : {one['name']}\n"
                      f"주소 : {one['addr']}\n"
                      f"{'='*20}")
        except:
            print("*** 입력 오류 ***")
            continue

    elif select == 3:
        hacbun = int(input("학번 입력 : "))
        one = info.get(hacbun)
        if one == None:    
            name = input("이름 입력 : ")
            addr = input("주소 입력 : ")
            one['name'] = name
            one['addr'] = addr
          # info.update({no : { 'name' : name , 'addr' : addr }}) 이렇게도 가능
            print("변경 완료!")
 
    elif select == 4:
        try:
            hacbun = int(input("학번 입력 : "))
            one = info.get(hacbun)
            if one == None:
                print("존재하지 않는 학번입니다.")
            else:
                name = input("이름 입력 : ")
                if one['name'] == name:
                    info.pop(hacbon)
                    print(f"{name}님의 정보 삭제 완료")
                else:
                    print("이름을 잘못 입력하셨습니다.")
        except:
            print("*** 입력 오류 ***")
            continue

    elif select == 5:
        for hacbun in info:
            one  = info.get(hacbun)
            print(f"{'='*20}\n"
                  f"학번 : {hacbun}\n"
                  f"이름 : {one['name']}\n"
                  f"주소 : {one['addr']}\n"
                  f"{'='*20}")

    elif select == 6:
        print("학적정보 조회 시스템이 종료되었습니다.")
        break
    else:
        print("번호를 잘못 입력하셨습니다.")
"""








