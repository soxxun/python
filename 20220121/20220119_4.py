from datetime import datetime
yourYear = int(input("태어난 년도 :"))
currentYear = datetime.today().year #현재 년도
age = currentYear - yourYear + 1
isStudent = True;

result = "학생이 아닙니다."
if age <= 26:
    if age >= 20:
        result = "대학생"
    elif age >= 17:
        result = "고등학생"
    elif age >= 14:
        result = "중학생"
    elif age >= 8:
        result = "초등학생"
    else:
        result = "학생이 아닙니다."
        isStudent = False
else:
    result = "학생이 아닙니다."
    isStudent = False

if isStudent:
    print(f"태어난 년도는 {yourYear} 이고 {result} 입니다.")
else:
    print(f"태어난 년도는 {yourYear} 이고 {result}.")