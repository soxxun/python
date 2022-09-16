
# 삭제하기
import os
# [os.remove(f) for f in glob.glob('Users/Python/my_web_scraping/*.jpg')]

# 확장자 여러 개 지정
def delete_jpg_png():
    pick_files = ['jpg', 'png']
    org_directory = os.getcwd()

    org_directory = org_directory.replace('\\', '/', 20)
    for i in range(len(pick_files)):
        fileList = os.listdir(org_directory)
        delete_num = [n for n in range(len(fileList)) if pick_files[i] in fileList[n]]
        for j in delete_num:
            os.remove(f'{org_directory}/{fileList[j]}')

delete_jpg_png()