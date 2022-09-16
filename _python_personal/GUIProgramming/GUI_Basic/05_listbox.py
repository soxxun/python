
from tkinter import *

# 초기 설정
root = Tk()
root.title('Soxxun GUI')
root.geometry("640x480") # 가로 X 세로

# 리스트 박스
# - 여러 줄에 걸쳐 어떤 목록을 관리하는 위젯
# - height값은 지정된 숫자만큼의 리스트 개수를 보여줌
listbox = Listbox(root, selectmode='extended', height=0) # 여러 개 선택 가능
# listbox = Listbox(root, selectmode='single', height=0) # 한 가지 선택 가능
listbox.insert(0, '사과')
listbox.insert(1, '딸기')
listbox.insert(2, '바나나')
# END를 사용하면 일일이 인덱스번호를 지정해 줄 필요가 없음
listbox.insert(END, '수박')
listbox.insert(END, '포도')
listbox.pack()

def btncmd():
    # 항목 삭제
    # listbox.delete(END) # 맨 뒤 항목 제거
    # listbox.delete(0) # 맨 앞 항목 제거

    # 개수 확인
    print(f'리스트에는 {listbox.size()}개가 있어요.')

    # 항목 확인 : get(시작 인덱스, 끝 인덱스)
    print(f'1번째부터 3번째까지의 항목 : {listbox.get(0,2)}')

    # 선택된 항목 확인 (인덱스값 반환)
    print(f'선택된 항목 : {listbox.curselection()}')

btn = Button(root, text='클릭', command=btncmd)
btn.pack()

root.mainloop()