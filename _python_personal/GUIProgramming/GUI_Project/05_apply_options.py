
'''
Project) 여러 이미지를 합치는 프로그램을 만드시오.

[사용자 시나리오]
1. 사용자는 합치려는 이미지를 1개 이상 선택한다.
2. 합쳐진 이미지가 저장될 경로를 지정한다.
3. 가로넓이, 간격, 포맷, 옵션을 지정한다.
4. 시작 버튼을 통해 이미지를 합친다.
5. 닫기 버튼을 통해 프로그램을 종료한다.

[기능 명세]
1. 파일추가 : 리스트 박스에 파일 추가
2. 선택삭제 : 리스트 박스에서 선택된 항목 삭제
3. 찾아보기 : 저장 폴더를 선택하면 텍스트 위젯에 입력
4. 가로넓이 : 이미지 넓이 지정 (원본유지, 1024, 800, 640)
5. 간격 : 이미지 간의 간격 지정 (없음, 좁게, 보통, 넓게)
6. 포맷 : 저장 이미지 포맷 지정 (PNG, JPG, BMP)
7. 시작 : 이미지 합치기 작업 실행
8. 진행상황 : 현재 진행중인 파일 순서에 맞게 반영
9. 닫기 : 프로그램 종료
'''

import os
import tkinter.ttk as ttk
from tkinter import * # __all__
from tkinter import filedialog # filedialog 는 서브 모듈이므로 한 번 더 명시해 주어야 import 됨
import tkinter.messagebox as msgbox
from PIL import Image

root = Tk()
root.title('MSY Photo')

# =================================== 함수 정의 ==========================================

# 파일 추가
def add_file():
    files = filedialog.askopenfilenames(title='이미지 파일을 선택하세요.',
                                        filetypes=(('PNG 파일', '*.png'), ('모든 파일', '*.*')), # 튜플 형태
                                        initialdir=r'C:\Users\pc\Desktop\Python\GUIProgramming\GUi_project') # 최초에 C:/ 경로를 보여줌
    # 사용자가 선택한 파일 가져오기
    for file in files:
        list_file.insert(END, file)


# 선택 삭제
def del_file():
    for idx in reversed(list_file.curselection()):
        list_file.delete(idx)

# 저장 경로 (출력 폴더 선택)
def browse_dest_path():
    folder_selected = filedialog.askdirectory() # 폴더 선택창
    if folder_selected == '': # is None으로 하면 return을 타지 않음. 즉 askdirectory()가 아무것도 없을 때 빈 문자열이 들어오므로 조건을 ''로 지정해 주어야 함
        return
    txt_dest_path.delete(0, END) # Entry이기 때문에 0이 시작점 (텍스트의 경우 0.1이 시작)
    txt_dest_path.insert(0, folder_selected)


# 이미지 통합
# noinspection PyTypeChecker
def merge_image():

# + 버그
# - 윈도우10에서는 C:/에는 직접적으로 바로 파일을 사용하는 것이 불가능하므로 관리자 권한이 필요한데, 이 프로그램에는 그러한 권한이 없기 때문에 작업이 실패함
# - 또한 존재하지 않는 저장경로를 적어줄 시에도 프로그램상에서는 아무런 문제가 없는 것처럼 보이지만 실제로는 Error
# --> try...except 구문 사용하기

    try:
        # 가로넓이
        img_width = cmb_width.get()
        if img_width == '원본유지':
            img_width = -1 # -1일 때는 원본 기준으로 이미지를 통합하라
        else:
            img_width = int(img_width)

        # 간격
        img_space = cmb_space.get()
        if img_space == '좁게':
            img_space = 30
        elif img_space == '보통':
            img_space = 60
        elif img_space =='넓게':
            img_space = 90
        else: # 없음
            img_space = 0

        # 포맷
        img_format = cmb_format.get().lower() # PNG, JPG, BMP 값을 받아와 소문자로 변환

        ###########################################################

        images = [Image.open(x) for x in list_file.get(0, END)]

        # 이미지 사이즈를 리스트에 넣어 하나씩 처리
        image_sizes = [] # (width1, height), (width2, height2), ...
        if img_width > -1:
            # width 값 변경
            image_sizes = [(int(img_width), int(img_width * x.size[1] / x.size[0])) for x in images]

        else:
            # 원본 사이즈 사용
            image_sizes = [(x.size[0], x.size[1]) for x in images]

        # 계산식
        # 100 * 60 이미지가 있음 --> width 를 80으로 줄이면 height 는?
        # (원본 width : 원본 height) = (변경 width : 변경 height)
        #     100    :     60      =      80     :      ?
        #      x     :      y      =      x'     :      y'
        # xy' = x'y
        # y' = x'y / x => 이 식을 적용
        # 100 : 60 = 80 : ?
        # y' = 48

        # 위 식을 코드에 대입하려면?
        # x = width = size[0]
        # y = height = size[1]
        # x' = img_width # 이 값으로 변경해야 함
        # y' = img_width * size[1] / size[0]

        # widths, heights = zip(*(x.size for x in images)) --> 실제로 변경된 값 적용
        widths, heights = zip(*(image_sizes))

        max_width, total_height = max(widths), sum(heights)
        print(f'max width : {max_width}\ntotal height : {total_height}')

        # 스케치북 준비
        if img_space > 0: # 이미지 간격 옵션 적용
            total_height += (img_space * (len(images) - 1))

        result_img = Image.new('RGB', (max_width, total_height), (255, 255, 255)) # 배경 : 흰색
        y_offset = 0 # 처음 이미지를 붙인 기점으로 순차적으로 다시 중앙에 위치시키기 위한 옵션 (x좌표는 그대로, y위치만 늘려가며 위치시키기)

        # progressbar
        for idx, img in enumerate(images): # (인덱스, 실제 이미지 데이터)
            # width가 원본유지가 아닐 때에는 이미지 크기 조정을 해 주어야 함
            if img_width > -1:
                img = img.resize(image_sizes[idx])

            result_img.paste(img, (0, y_offset))
            y_offset += (img.size[1] +  img_space) # height + 사용자가 지정한 간격

            progress = (idx + 1) / len(images) * 100 # 실제 퍼센트 정보를 계산
            p_var.set(progress) # progressbar + progress값 매핑
            progressbar.update() # UI 업데이트

        # 포맷 옵션 처리
        file_name = 'MSY Photo.' + img_format

        # 실제 이미지 저장 경로
        dest_path = os.path.join(txt_dest_path.get(), 'MSY Photo.jpg') # 입력 받은 파일 경로(Entry), 저장할 파일 이름
        result_img.save(dest_path)
        msgbox.showinfo('알림', '작업이 완료되었습니다.')

    except Exception as err:
        msgbox.showerror('에러', err)

# 시작
def start():
    # 각 옵션들 값 확인
    print(f'가로넓이 : {cmb_width.get()}') # .get()을 해주지 않으면 속성값이 출력됨
    print(f'간격 : {cmb_space.get()}')
    print(f'포맷 : {cmb_format.get()}')

    # 파일 목록 확인
    if list_file.size() == 0: # 하나의 파일도 선택되지 않았다면
        msgbox.showwarning('경고', '이미지 파일을 추가하세요.')
        return

    # 저장 경로 확인
    if len(txt_dest_path.get()) == 0: # 문자열의 길이가 0일 때, 즉 엔트리 내부에 아무 것도 없을 때
        msgbox.showwarning('경고', '저장 경로를 선택하세요.')
        return

    # 이미지 통합 작업
    merge_image()

# ===========================================================================================

# 파일 프레임 (파일추가, 선택삭제)
file_frame = Frame(root)
file_frame.pack(fill='x', padx=5, pady=5) # 가로로 펼쳐지도록 채워지도록 지정

btn_add_file = Button(file_frame, padx=5, pady=5, width=12, text='파일추가', command=add_file)
btn_add_file.pack(side='left')

btn_del_file = Button(file_frame, padx=5, pady=5, width=12, text='선택삭제', command=del_file)
btn_del_file.pack(side='right')

# 지금은 프레임이 두 개 뿐이기 대문에 붙어있지만 차차 만들면서 벌어지게 되는 것임

# 리스트 프레임
list_frame = Frame(root)
list_frame.pack(fill='both', padx=5, pady=5)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side='right', fill='y')

list_file = Listbox(list_frame, selectmode='extended', height=15, yscrollcommand=scrollbar.set)
list_file.pack(side='left', fill='both', expand=True)
scrollbar.config(command=list_file.yview)
# 리스트 박스도 스크롤바를 매핑하고 스크롤바도 리스트 박스를 매핑하도록 준 것

# 저장 경로 프레임
path_frame = LabelFrame(root, text='저장경로')
path_frame.pack(fill='x', padx=5, pady=5, ipady=5)

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side='left', fill='x', expand=True, padx=5, pady=5, ipady=4) # ipad : 엔트리의 크기를 살짝 높여주는 효과 (안쪽 패딩)

btn_dest_path = Button(path_frame, text='찾아보기', width=10, command=browse_dest_path)
btn_dest_path.pack(side='right', padx=5, pady=5)

# 옵션 프레임
frame_option = LabelFrame(root, text='옵션')
frame_option.pack(padx=5, pady=5, ipady=5)


# 1. 가로 넓이 옵션
# 가로 넓이 레이블
lbl_width = Label(frame_option, text='가로넓이', width=8)
lbl_width.pack(side='left', padx=5, pady=5)
# side를 주지 않으면 위에서 아래 방향으로 하나씩 쌓여버림
# 2. 가로 넓이 콤보
opt_width = ['원본유지', '1024', '800', '640']
cmb_width = ttk.Combobox(frame_option, state='readonly', values=opt_width, width=10)
cmb_width.current(0) # 0번째 인덱스 자동 선택
cmb_width.pack(side='left', padx=5, pady=5)


# 2. 간격 옵션
# 간격 옵션 레이블
lbl_space = Label(frame_option, text='간격', width=8)
lbl_space.pack(side='left', padx=5, pady=5)
# 간격 옵션 콤보
opt_space = ['없음', '좁게', '보통', '넓게']
cmb_space = ttk.Combobox(frame_option, state='readonly', values=opt_space, width=10)
cmb_space.current(0) # 0번째 인덱스 자동 선택
cmb_space.pack(side='left', padx=5, pady=5)


# 3. 파일 포맷 옵션
# 파일 옵션 레이블
lbl_format = Label(frame_option, text='포맷', width=8)
lbl_format.pack(side='left', padx=5, pady=5)
# 파일 옵션 콤보
opt_format = ['PNG', 'JPG', 'BMP']
cmb_format = ttk.Combobox(frame_option, state='readonly', values=opt_format, width=10)
cmb_format.current(0) # 0번째 인덱스 자동 선택
cmb_format.pack(side='left', padx=5, pady=5)


# 진행 상황 Progress Bar
frame_progress = LabelFrame(root, text='진행상황')
frame_progress.pack(fill='x', padx=5, pady=5, ipady=5)

p_var = DoubleVar()
progressbar = ttk.Progressbar(frame_progress, maximum=100, variable=p_var)
# variable : 실제값과 프로그레스바를 매핑시킨 것
progressbar.pack(fill='x', padx=5, pady=5)

def close():
    root.quit()

# 실행 프레임 (시작/닫기)
frame_run = Frame(root)
frame_run.pack(fill='x', padx=5, pady=5)

btn_close = Button(frame_run, padx=5, pady=5, text='닫기', width=12, command=close)
btn_close.pack(side='right', padx=5, pady=5)

btn_start = Button(frame_run, padx=5, pady=5, text='시작', width=12, command=start)
btn_start.pack(side='right', padx=5, pady=5)

# 닫기 버튼을 먼저 작성하여 오른쪽에 배치하여야 시작 -> 닫기 순으로 나타난다.

root.resizable(False, False)
root.mainloop()














