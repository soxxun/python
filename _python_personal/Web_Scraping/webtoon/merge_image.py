import os
from tkinter import *
import tkinter as tk
from tkinter import filedialog
import tkinter.messagebox as msgbox
from PIL import Image, ImageColor
import glob

def merge_image():
    try:
        root = Tk()
        root.title('MSY PHOTONARA')
        root.geometry('385x700')

        target_dir = '/Users/pc/Desktop/Python/Web_scraping/my_web_scraping/'
        files = glob.glob(target_dir + '*.jpg')
        file_list = []
        num = 0

        for file in files:
            path = f'/Users/pc/Desktop/Python/Web_scraping/my_web_scraping\\webtoon_images_{num}.jpg'
            file_list.append(path)
            num += 1
        # print(file_list)

        images = [Image.open(x) for x in file_list]

        widths = []
        heights = []

        for img in images:

            max_iter = img.size[0]

            if img.size[0] > max_iter:
                max_iter = img.size[0]

            if img.size[0] != max_iter:
                widths.append(int(img.size[0])*0.5)
                heights.append((int(img.size[0] * images[0].size[1]) / images[0].size[0])*0.5)
            else:
                widths.append(int(img.size[0]*0.5))
                heights.append(int(img.size[1]*0.5))

        max_width, max_height, total_height = max(widths), max(heights), sum(heights)
        # total_height += (10 * (len(images) - 1))

        img_clr = ImageColor.getcolor('white', 'RGB')
        result_img = Image.new("RGB", (max_width, total_height), img_clr)
        y_offset = 0

        num = 0
        for img in images: # (인덱스, 실제 이미지 데이터)
            img = img.resize((widths[num], heights[num]))
            result_img.paste(img, (0, y_offset))
            y_offset += int(img.size[1])
            num += 1

        dest_path = os.path.join(os.getcwd(), 'result_img.png') # 저장할 파일 경로, 저장할 파일 이름
        result_img.save(dest_path, 'png')
        # re = Image.open('result_img.png', 'r')
        # re.show()

        # 캔버스
        canvas = Canvas(root, bg='white', width=max_width, height=total_height, scrollregion=(0, 0, max_width, total_height))
        img_path = PhotoImage(file='/Users/pc/Desktop/Python/Web_scraping/my_web_scraping/result_img.png')
        canvas.create_image(10, 10, anchor='nw', image=img_path)

        # 스크롤바
        hbar = Scrollbar(canvas, orient=HORIZONTAL)
        hbar.pack(side=BOTTOM, fill=X)
        hbar.config(command=canvas.xview)

        vbar = Scrollbar(canvas, orient=VERTICAL)
        vbar.pack(side=RIGHT, fill=Y)
        vbar.config(command=canvas.yview)

        canvas.config(width=max_width, height=total_height)
        canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
        canvas.bind('<MouseWheel>')
        canvas.pack(side=LEFT, expand=True, fill=BOTH)

        # 스크롤바 <-> 마우스휠 binding
        def MouseWheelHandler(event):
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

        root.bind("<MouseWheel>", MouseWheelHandler)
        root.resizable(True, True)
        msgbox.showinfo('알림', '작업이 완료되었습니다.')

        root.mainloop()
    except Exception as e:
        print(f'이미지를 가져올 수 없습니다.')
merge_image()


