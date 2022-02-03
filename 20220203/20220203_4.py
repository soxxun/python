import random
nameList = list("가나다라마바사아자차카타파하")
sungList = list("김이박최홍")
with open("info.txt","w") as f:
    for i in range(1000):
        name = random.choice(nameList)+random.choice(nameList)
        sung = random.choice(sungList)
        name = sung + name
        weight = random.randrange(40,100)
        height = random.randrange(140, 200)
        f.write(f"{name},{weight},{height}\n")

# read file
# bmi
with open("info.txt","r") as f:
    for line in f:
        print(line)
        (name,weight,height) =  line.split(",")
        height = int(height)*0.01
        bmi = int(weight) / (height**2)
        result = ""
        if bmi >= 25:
            result = "과체중"
        elif bmi >= 18.5:
            result = "정상"
        else:
            result = "저체중"
        # print(f"이름:{name}\n몸무게:{weight}\n키:{height}\nBMI:{bmi}\n결과:{result}")
        print(
            "\n".join([f"이름:{name}",
                       f"몸무게:{weight}",
                       f"키:{height}",
                       f"BMI:{bmi}",
                       f"결과:{result}"]
                      )
        )
