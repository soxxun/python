# description : 문자열중에 특정 문자가있는지 검사하는 함수
# 매개변수는 : 문자열, 특정문자
# 린턴 : 문자열에 해당되는문자가 있으면 True 없으면 False
def checkIncludeCharacter(targetStr, findStr):
    checked = False
    for character in targetStr:
        if character in findStr:
            checked = True
            break
    return checked


# description : 문자열과 true/false의 값을 받아서  true이면 way를 붙여준다
def mergeStr(strs, isAppend):
    result = ""
    if isAppend:
        result = strs + " way"
    else:
        result = strs
    return result


compare = "aeiou"
sentense = "hello pyth easy"
splitSentense = sentense.split()
# ['hello', 'pyth', 'easy']

# main process
for strs in splitSentense:
    checked = checkIncludeCharacter(strs,compare)
    strs = mergeStr(strs,checked)
    print(strs)
