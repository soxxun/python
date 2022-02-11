# 클래스
#   변수 : 특징, 속성 , 상태
#   함수 : 변수를 가지고 구현한 로직 or 클래스의 특징을 나타내는 메소드

# 사각형
#   변수 : 가로의길이 세로의길이
#   함수 : 넓이

class Rectangle:
    def __init__(self,width=0,height=0):
        if (width < 0) or (height < 0):
            raise ValueError("양수만 입력하세요")
        self.__width = width
        self.__height = height
    def area(self):
        return self.__width * self.__height
    def get_width(self):
        return self.__width
    def get_height(self):
        return self.__height
    def set_width(self,width):
        if width < 0:
            raise ValueError("0보다 커야 합니다.")
        self.__width = width
    def set_height(self,height):
        if height < 0:
            raise ValueError("0보다 커야 합니다.")
        self.__height = height

# 논리적으로 성립이 안됨
r = Rectangle()
r.__width = 100
print(r.area())
