
from tkinter import *

# 초기 설정
root = Tk()
root.title('Soxxun GUI')
root.geometry("640x480") # 가로 X 세로

# 체크 박스
chkvar = IntVar() # chkvar에 int형으로 값 저장하기
chkbox = Checkbutton(root, text='오늘 하루 보지 않기', variable=chkvar) # 체크박스 필수 매개변수
# chkbox.select() # 자동 선택 처리
# chkbox.deselect() # 선택 해제 처리
chkbox.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text='일주일 동안 보지 않기', variable=chkvar2)
chkbox2.pack()

def btncmd():
    print(chkvar.get()) # 0 : 체크 해제, 1 : 체크
    print(chkvar2.get())

btn = Button(root, text='클릭', command=btncmd)
btn.pack()

root.mainloop()