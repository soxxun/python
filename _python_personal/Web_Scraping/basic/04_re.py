'''
정규식

주민등록번호
970501-1111111

이메일 주소
soxxun@naver.com

차량 번호
11가 1234

IP 주소
192.168.0.1

이런 식으로 정해진 형태에 부합한지 아닌지를 구분하기 위해 사용하는 것이 정규식이다.
매우 복잡하고 어려워 숙련자들에게도 쉽지 않다.
'''

import re

# 차량 번호가 네 자리 문자 형식이라고 가정

# ca?e --> 문자 한 개가 기억이 나지 않을 땐?
# a~z까지 ... X 경우의 수가 매우 많을 때는 용이하지 않음

# . (ca.e) : 하나의 문자를 의미 (ex. care, cafe, case | caffe X)
# ^ (^de) : 문자열의 시작을 의미 (ex. desk, destination | fade X)
# $ (se$) : 문자열의 끝을 의미 (ex. case, base, raise | face X)


# 패턴값 받아오기
p = re.compile("ca.e")

'''
# 패턴과 매칭되는지 확인
m = p.match("case")
# print(m.group()) # 매치되지 않으면 에러 발생

if m:
    print(m.group())
else:
    print('매칭되지 않았습니다.')
'''

# 함수로 정의
def print_match(m):
    if m:
        print(f'm.group : {m.group()}') # 일치하는 문자열 반환
        print(f'm.string : {m.string}') # 입력받은 문자열 반환
        # string은 함수가 아니라 변수이기 때문에 괄호 없이 사용해야 함
        print(f'm.start : {m.start()}') # 일치하는 문자열의 시작 인덱스
        print(f'm.end : {m.end()}') # 일치하는 문자열의 끝 인덱스
        print(f'm.span : {m.span()}') # 일치하는 문자열의 시작 / 끝 인덱스
    else:
        print('매칭되지 않았습니다.')

# m = p.match("careless") # 주어진 문자열의 처음부터 일치하는지 확인 (즉 뒤에 다른값들이 있어도 처음부터 정확히 일치하므로 정상 작동)
# print_match(m)

# search : 주어진 문자열 중에 일치하는 문자가 있는지 확인
# m = p.search('good care')
# print_match(m)

# findall : 일치하는 모든 것을 리스트 형태로 반환
# lst = p.findall('good care cafe')
# print(lst)

'''
1. p = re.compile('원하는 형태')
2. m = p.match('비교할 문자열') : 주어진 문자열의 처음부터 일치하는지 확인
3. m = p.search('비교할 문자열') : 주어진 문자열 중 일치하는 게 있는지 확인
4. lst = p.findall('비교할 문자열') : 일치하는 모든 것을 "리스트" 형태로 반환

(원하는 형태)
 . (ca.e) : 하나의 문자를 의미 (ex. care, cafe, case | caffe X)
 ^ (^de) : 문자열의 시작을 의미 (ex. desk, destination | fade X)
 $ (se$) : 문자열의 끝을 의미 (ex. case, base, raise | face X)
'''

# 정규식에 대해 더 공부하고 싶을 때
# 1. http://www.w3school.com
# 2. LEARN PYTHON
# 3. Python RegEx

# OR 구글에 python re 검색
# 1. docs.python.org
# 2. 원하는 내용 검색 후 예제와 설명 참고