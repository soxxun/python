
from tkinter import *

# 초기 설정
root = Tk()
root.title('Soxxun GUI')
root.geometry("640x480")

label1 = Label(root, text='안녕하세요')
label1.pack()

photo = PhotoImage(file=r'C:\Users\pc\Desktop\Python\GUIProgramming\GUI_basic\img.png')
label2 = Label(root, image=photo)
label2.pack()

def change():
    label1.config(text='또 만나요') # label의 원래 값을 바꿔줌
    global photo2
    photo2 = PhotoImage(file=r'C:\Users\pc\Desktop\Python\GUIProgramming\GUI_basic\img2.png')
    label2.config(image=photo2)
    # 전역변수로 만들어 주어야 Garbage Collection에 걸려 지워지지 않음

btn = Button(root, text='클릭', command=change)
btn.pack()


root.mainloop() # 창이 닫히지 않도록 해 줌