'''
Quiz) tkinter을 이용한 메모장 프로그램을 만드시오.

1. title : 제목 없음 - window 메모장
2. 메뉴 : 파일, 편집, 서식, 보기, 도움말
3. 실제 메뉴 구현 : 파일 메뉴 내에서 열기, 저장, 끝내기 3개만 처리
3-1. 열기 : mynote.txt 파일 내용 열어서 보여주기
3-2. 저장 : mynote.txt 파일 현재 내용 저장하기
3-3. 끝내기 : 프로그램 종료
4. 프로그램 시작 시 본문은 비어 있는 상태
5. 하단 status 바는 필요 없음
6. 프로그램 크기, 위치는 자유롭게 하되 크기 조정 가능해야 함
7. 본문 우측에 상하 스크롤 바 넣기
'''

import os # 파일 존재 여부 체크
from tkinter import *

root = Tk()
root.title('제목 없음 - window 메모장')
root.geometry('640x550')

fileName = 'mynote.txt'

# 파일 열기
def open_file():
    if os.path.isfile(fileName): # 있으면 True, 없으면 False
        with open(fileName, 'r', encoding='utf8') as f:
            txt.delete('1.0', END) # 텍스트 위젯 본문 삭제
            txt.insert(END, f.read()) # 읽어들이기

# 파일 저장
def save():
    with open(fileName, 'w', encoding='utf8') as f:
        f.write(txt.get('1.0', END))


# 파일 메뉴
menu = Menu(root)
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label='새로 만들기(N)', state='disable')
menu_file.add_command(label='새 창(W)', state='disable')
menu_file.add_command(label='열기(D)', command=open_file)
menu_file.add_command(label='저장(S)', command=save)
menu_file.add_command(label='다른 이름으로 저장(A)', state='disable')
menu_file.add_separator()
menu_file.add_command(label='페이지 설정(U)', state='disable')
menu_file.add_command(label='인쇄(P)', state='disable')
menu_file.add_command(label='끝내기(X)', command=root.quit)
menu.add_cascade(label='파일', menu=menu_file)


# 편집 / 서식 / 보기 / 도움말 메뉴
menu.add_cascade(label='편집')
menu.add_cascade(label='서식')
menu.add_cascade(label='보기')
menu.add_cascade(label='도움말')
root.config(menu=menu)

# 스크롤 바
# - 이전에는 같은 프레임에 넣으면 리스트박스와 스크롤바가 매핑되어 가능했으나,
# - 여기에서는 위젯이 없고 텍스트 하나만 있기 때문에 루트를 바로 넣어도 됨 (즉 루트를 하나의 프레임으로 취급)
scrollbar = Scrollbar(root)
scrollbar.pack(side='right', fill='y') # y 방향으로 스크롤바 채우기

# 메모 입력 공간
txt = Text(root, yscrollcommand=scrollbar.set) # 텍스트 매핑
txt.pack(side='left', fill='both', expand=True) # 입력 공간 전체로 채우기

# 스크롤바 매핑
scrollbar.config(command=txt.yview)

root.mainloop()


