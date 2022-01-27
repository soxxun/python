stc = "Hello Python ! :)"
compare = "aeiou"
splitStc = stc.split()
# ['hello', 'Python', '!', ':)']

# 함수명 : description : 문자열 중 특정 문자가 있는지 검사하는 함수
# 매개변수 : 문자열과 검사하려는 특정 문자열
# 리턴 : 문자열에 해당되는 문자가 있으면 True, 없으면 False

def checkIncludeCharacter(targetStr, findStr):
    checked = False # 초기값을 False로 해야 True일 때 True를 반환
    for character in targetStr:
        if character in findStr:
            checed = True
            break
    return checked

# description : 문자열과 T/F의 값을 받아 True이면 way를 붙여줌
def mergeStr(strs, isAppend):
    result = ""
    if isAppend:
        result = strs + " way"
    else:
        result = strs
    return result

for strs in splitStc:
    checked = checkIncludeCharacter(strs, compare)
    strs = mergeStr(strs, checked)
    print(strs)