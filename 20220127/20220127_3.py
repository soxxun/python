# 공백으로 구분된문장
# split() 함수를이용  --> 문장을 공백을기준으로 나눠서 리스트로 반환
# 특정 값이나 문자가 리스트에 있는지 여부를판단하는 기능 in

compare = "aeiou"
sentense = "hello pyth easy"
splitSentense = sentense.split()
# ['hello', 'pyth', 'easy']
for strs in splitSentense:
    checked = False
    for character in strs:
        if character in compare:
            checked = True
    if checked:
        print(f"{strs} way")
    else:
        print(strs)






