# 중첩 if 문

isFirst, isSecond = True, False

if isFirst:
    print(f"첫번째 if 문장 isFirst={isFirst}")
    if isSecond:
        print(f"두번째 if 문장  isFirst={isFirst} isSecond = {isSecond}")
    else:
        print(f"두번째 if 문의 else  isFirst={isFirst} isSecond = {isSecond}")

