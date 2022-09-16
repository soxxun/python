
import time
import tkinter.ttk as ttk # progressbar
from tkinter import *

# 초기 설정
root = Tk()
root.title('Soxxun GUI')
root.geometry("640x480") # 가로 X 세로

'''
# 진행방식 표시
# progressbar = ttk.Progressbar(root, maximum=100, mode='indeterminate') # 언제 끝날지 모르는 작업 시
progressbar = ttk.Progressbar(root, maximum=100, mode='determinate')
progressbar.start(10) # 10ms 마다 움직임
progressbar.pack()

def btncmd():
    progressbar.stop() # 작동 중지

btn = Button(root, text='중지', command=btncmd)
btn.pack()
'''
p_var2 = DoubleVar() # %는 늘 정수값으로 올라가는 것이 아니기 때문에 실수값도 반영하기 위해 더블값 지정
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()

def btncmd2():
    for i in range(1,101): # 1~100
        time.sleep(0.01) # 0.01초 대기
        p_var2.set(i) # progressbar의 값 설정
        progressbar2.update() # 시각적으로 보기 위해 매번 ui 업데이트
        if p_var2.get() == 50:
            print('50% 이상 완료되었습니다.')
        elif p_var2.get() == 90:
            print('90% 이상 완료되었습니다.')
    print('모든 작업이 완료되었습니다.')

btn = Button(root, text='시작', command=btncmd2)
btn.pack()

root.mainloop()