
import tkinter.ttk as ttk # 콤보박스
from tkinter import *

# 초기 설정
root = Tk()
root.title('Soxxun GUI')
root.geometry("640x480") # 가로 X 세로

values = [str(i) + '일' for i in range(1,32)] # 날짜
combobox = ttk.Combobox(root, height=5, values=values)
combobox.pack()
combobox.set('카드 결제일') # 최초 목록 제목 설정

readonly_combobox = ttk.Combobox(root, height=10, values=values, state='readonly')
readonly_combobox.current(0)
readonly_combobox.pack()

def btncmd():
    print(combobox.get())
    print(readonly_combobox.get())

btn = Button(root, text='선택', command=btncmd)
btn.pack()

root.mainloop()