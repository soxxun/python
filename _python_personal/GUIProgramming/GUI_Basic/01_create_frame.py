
from tkinter import *

# 초기 설정
root = Tk()

root.title('Soxxun GUI')
# root.geometry("640x480") # 가로 X 세로
root.geometry("640x480+300+100") # 가로 X 세로 + x좌표 + y좌표

root.wm_resizable(True, False) # x(너비), y(높이) 좌표 값 변경 불가 (창 크기 변경 불가)

root.mainloop() # 창이 닫히지 않도록 해 줌
