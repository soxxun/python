
from tkinter import *

# 초기 설정
root = Tk()
root.title('Soxxun GUI')
root.geometry("640x480") # 가로 X 세로

Label(root, text='메뉴를 선택해 주세요.').pack(side='top')
Button(root, text='주문하기').pack(side='bottom')

# 햄버거 가게 방문
frame_burger = LabelFrame(root, text='햄버거', relief='solid', bd=1) # bd : 외곽선 표시
frame_burger.pack(side='left', fill='both', expand=True)

Button(frame_burger, text='햄버거').pack()
Button(frame_burger, text='치즈버거').pack()
Button(frame_burger, text='치킨버거').pack()

frame_drink = LabelFrame(root, text='음료', relief='solid', bd=1)
frame_drink.pack(side='right', fill='both', expand=True)
Button(frame_drink, text='콜라').pack()
Button(frame_drink, text='사이다').pack()

root.mainloop()
