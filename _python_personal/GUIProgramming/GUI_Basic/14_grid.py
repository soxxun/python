
from tkinter import *

# 초기 설정
root = Tk()
root.title('Soxxun GUI')
root.geometry("640x480") # 가로 X 세로

# btn1 = Button(root, text='버튼1')
# btn2 = Button(root, text='버튼2')
# # btn1.pack()
# # btn2.pack()
# # btn1.pack(side='left')
# # btn2.pack(side='left')
#
# # 그리드로 넣기
# btn1.grid(row=0, column=0)
# btn2.grid(row=1, column=1)

# =====================================

# sticky = 지정한 방향으로 위젯을 쫙 늘린 후 붙여줌
# padx, pady --> Button : 버튼 크기 / grid : 그리드 간격
# 일괄 적용 : 찾을 범위 지정 - Ctrl+Shift+Alt+j - 수정 - 일괄 적용

# enter 때문에 f16 버튼만 간격이 넓음
# 이럴 때는 고정 크기값을 줄 수 있는 width, height값으로 설정하면 됨

# 맨 윗줄
btn_f16 = Button(root, text='F16', width=5, height=2)
btn_f17 = Button(root, text='F17', width=5, height=2)
btn_f18 = Button(root, text='F18', width=5, height=2)
btn_f19 = Button(root, text='F19', width=5, height=2)

btn_f16.grid(row=0, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_f17.grid(row=0, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_f18.grid(row=0, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_f19.grid(row=0, column=3, sticky=N+E+W+S, padx=3, pady=3)

# clear 줄
btn_clear = Button(root, text='clear', width=5, height=2)
btn_equal = Button(root, text='=', width=5, height=2)
btn_div = Button(root, text='/', width=5, height=2)
btn_mul = Button(root, text='*', width=5, height=2)

btn_clear.grid(row=1, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_equal.grid(row=1, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_div.grid(row=1, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_mul.grid(row=1, column=3, sticky=N+E+W+S, padx=3, pady=3)

# 7 시작줄
btn7 = Button(root, text='7', width=5, height=2)
btn8 = Button(root, text='8', width=5, height=2)
btn9 = Button(root, text='9', width=5, height=2)
btn_sub = Button(root, text='-', width=5, height=2)

btn7.grid(row=2, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn8.grid(row=2, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn9.grid(row=2, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_sub.grid(row=2, column=3, sticky=N+E+W+S, padx=3, pady=3)

# 4 시작줄
btn4 = Button(root, text='4', width=5, height=2)
btn5 = Button(root, text='5', width=5, height=2)
btn6 = Button(root, text='6', width=5, height=2)
btn_add = Button(root, text='+', width=5, height=2)

btn4.grid(row=3, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn5.grid(row=3, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn6.grid(row=3, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_add.grid(row=3, column=3, sticky=N+E+W+S, padx=3, pady=3)

# 1 시작줄
btn1 = Button(root, text='1', width=5, height=2)
btn2 = Button(root, text='2', width=5, height=2)
btn3 = Button(root, text='3', width=5, height=2)
btn_enter = Button(root, text='enter', width=5, height=2) # 세로로 합쳐짐

btn1.grid(row=4, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn2.grid(row=4, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn3.grid(row=4, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_enter.grid(row=4, column=3, rowspan=2, sticky=N+E+W+S, padx=3, pady=3) # 현재 row로부터 2개를 합침

# 0 시작줄
btn0 = Button(root, text='0', width=5, height=2)
btn_point = Button(root, text='.', width=5, height=2)

btn0.grid(row=5, column=0, columnspan=2, sticky=N+E+W+S, padx=3, pady=3)
btn_point.grid(row=5, column=2, sticky=N+E+W+S, padx=3, pady=3)

root.mainloop()