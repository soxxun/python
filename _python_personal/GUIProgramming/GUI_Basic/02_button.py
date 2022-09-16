
from tkinter import *

# 초기 설정
root = Tk()
root.title('Soxxun GUI')

btn1 = Button(root, text='버튼1')
btn1.pack() # 실제 메인 윈도우(root)에 적용시키기

btn2 = Button(root, padx=5, pady=10, text='버튼2')
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text='버튼3')
btn3.pack()

btn4 = Button(root, width=10, height=3, text='버튼4')
btn4.pack()

# padx, pady --> 문자가 차지하는 공간 상하좌우로 지정한값 만큼의 여백 확보
# width, height --> 문자 수와 상관 없이 고정된 크기값

btn5 = Button(root, fg='red', bg='yellow', text='버튼5')
btn5.pack()

photo = PhotoImage(file=r'C:\Users\pc\Desktop\Python\GUIProgramming\GUI_basic\img.png')
btn6 = Button(root, image=photo)
btn6.pack()

def btncmd():
    print('버튼이 클릭되었습니다.')

btn7 = Button(root, text='동작하는 버튼', command=btncmd)
btn7.pack()



root.mainloop() # 창이 닫히지 않도록 해 줌

