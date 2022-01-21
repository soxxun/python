#Dictionary
# 학생1명
# 이름,  점수(국 영 수)  주소

s1 = {
    "name" : "이규영",
    "score" : {
        "kor" : 95,
        "eng" : 98,
        "math" : 100
    },
    "addr" : "경기도 용인시"
}
s2 = {
    "name" : "홍길동",
    "score" : {
        "kor" : 99,
        "eng" : 98,
        "math" : 100
    },
    "addr" : "조선팔도"
}
# 데이터가 여려개다...???
students = [s1, s2]

# 학생들의 이름만 출력해 봅시다
# hint : for , dictionary[key]
for d in students:
    print(f"{d['name']} 의 영어 점수는 {d['score']['eng']}")


# list vs dctionary
# 요소들의 집합
# key:value 의 집합

# 값을 추가 새로운 키를 만들고 값을 대입
s1["rank"] = 'A'
print(s1)
s1["addr"] = "서울시 구로구"
print(s1)
del s1['rank']
print(s1)