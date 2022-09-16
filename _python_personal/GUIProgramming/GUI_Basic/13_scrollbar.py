
from tkinter import *

# 초기 설정
root = Tk()
root.title('Soxxun GUI')
root.geometry("640x480") # 가로 X 세로

# 스크롤 바와 그 대상이 되는 위젯을 하나의 프레임에 넣어두는 것이 편리
frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side='right', fill='y') # y 방향으로 스크롤바 채우기

listbox = Listbox(frame, selectmode='extended', height=10, yscrollcommand=scrollbar.set)
# yscrollcommand 설정을 해주지 않으면 스크롤바가 튕기듯이 위로 원위치 되어버림
for i in range(1, 31):
    listbox.insert(END, str(i) + '일')
listbox.pack(side='left')

scrollbar.config(command=listbox.yview)

root.mainloop()