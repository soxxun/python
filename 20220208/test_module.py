# 함수들을 정의
PI = 3.14
def number_input():
    number = input("숫자 입력")
    try:
        return float( number)
    except Exception as e:
        print(e)

def circleArea(radius):
    return 2 * PI * radius

def circleVolume(radius):
    return PI*radius**2

if __name__ == '__main__':
    print(f"circleArea(10) = {circleArea(10)}")
    print(f"circleVolume(10) = {circleVolume(10)}")