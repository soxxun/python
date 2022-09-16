
from tkinter import *

# 초기 설정
root = Tk()
root.title('Soxxun GUI')
root.geometry("640x480") # 가로 X 세로

# 라디오 버튼 (택 1) : 한 가지를 선택하면 다른 한 가지는 선택 해제됨
# - 햄버거 메뉴
label1 = Label(root, text='메뉴를 선택하세요.').pack()

burger_var = IntVar()
btn_burger1 = Radiobutton(root, text='햄버거', value=1, variable=burger_var)
# 기본값 설정
btn_burger1.select()
btn_burger2 = Radiobutton(root, text='치즈버거', value=2, variable=burger_var)
btn_burger3 = Radiobutton(root, text='치킨버거', value=3, variable=burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

# - 음료 메뉴
Label(root, text='음료를 선택하세요.').pack()

drink_var = StringVar()
btn_drink1 = Radiobutton(root, text='콜라', value='콜라', variable=drink_var)
btn_drink1.select()
btn_drink2 = Radiobutton(root, text='사이다', value='사이다', variable=drink_var)

btn_drink1.pack()
btn_drink2.pack()

def btncmd():
    print(burger_var.get()) # 선택된 라디오 항목의 값(value)을 출력
    print(drink_var.get())

btn = Button(root, text='클릭', command=btncmd)
btn.pack()

root.mainloop()