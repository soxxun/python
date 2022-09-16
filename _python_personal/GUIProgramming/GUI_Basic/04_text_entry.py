
from tkinter import *

# 초기 설정
root = Tk()
root.title('Soxxun GUI')
root.geometry("640x480") # 가로 X 세로

txt = Text(root, width=30, height=5)
txt.pack()

# 기본 설정값
txt.insert(END,'글자를 입력하세요.')

# entry
# - 주로 아이디/비밀번호 입력 시 사용
e = Entry(root, width=30)
e.pack()
e.insert(0, '한 줄만 입력하세요.')

def btncmd():
    # 텍스트에 있는 값 가져오기
    print(txt.get('1.0', END)) # 처음부터 끝까지 모든 텍스트 가져오기
                 # 1 - 라인 / 0 - 컬럼 위치
    # 엔트리에 있는 값 가져오기
    print(e.get())

    # 글자를 가져오고 나서 값 지우기
    txt.delete('1.0', END)
    e.delete(0, END)

btn = Button(root, text='클릭', command=btncmd)
btn.pack()

root.mainloop() # 창이 닫히지 않도록 해 줌