# 합격자 조회하기 Businees Logic
# DataBase 연동.......
# DB 접속을 해서 합격자 table 을 조회한후 결과를 리스트로 반환
successLists = ['홍길동', '이순신', '철이', '미애', '이규영']
# 합격자 명단에 '이름'이 있는지 조회

name = input("이름 : ")
if name in successLists:
    print(f"축하합니다. {name}님 합격하셨습니다.")
else:
    print("아쉽지만 다음기회....")