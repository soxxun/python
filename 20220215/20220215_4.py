#회문 검사
# 역삼역   mom
# 기러기  wow
# 일요일   noon
# queue : 줄 서기, 기차가 터널을 들어가서 빠져나오는  First In First Out  FIFO
# stack " Fisrt In Last Out FILO

# 큐
qu = []
qu.append(1)
qu.append(2)
qu.append(3)
print(qu.pop(0))
print(qu.pop(0))
print(qu.pop(0))
print(len(qu))

#스택
st = []
st.append(1)
st.append(2)
st.append(3)
print(st.pop())
print(st.pop())
print(st.pop())
print(len(qu))

# 회문 검사
# 대소문자 구분 안함  공백구분 안함, 알파벳만 구분
# Wow   회문
# 다시 합창 합시다
# Madam, I'm Adam   MadamImAdam

# 데이터를 입력할때 해당 문자가 알파벳이면(공백, 특수문자, 숫자가 아니면) 큐와  스택에 입력
# isalpha() --> 알파벳


qu = []  # 큐 자료구조
st = []  # 스택 자료구조
# 데이터 입력단계
# for i in data:
#     if i.isalpha():
#         qu.append(i.upper())
#         st.append(i.upper())

# 2단계 : 스택과 큐의 성질을 이용해서 회문여부 판단
data = input("회문을 입력하세요")
def isSame(data):
    qu = []  # 큐 자료구조
    st = []  # 스택 자료구조
    for i in data:
        if i.isalpha():
            qu.append(i.upper())
            st.append(i.upper())
    while qu:
        if qu.pop(0) != st.pop():
            return False
    return True
print('회문입니다.') if isSame(data)  else print("회문이 아닙니다.")

