
# 시간별 처리

import time
from PIL import ImageGrab # 파이썬 라이브러리

# 프로그램 실행 후 5초 대기 (셋팅 시간)
# 2초에 한 번씩 총 10번의 스크린샷 및 파일 저장 프로그램

time.sleep(5)

for i in range(1,11): # 2초 간격으로 10개 이미지 저장
    img = ImageGrab.grab() # 현재 스크린 이미지를 가져옴
    img.save(f'image{i}.png') # image1.png ~ image10.png
    time.sleep(2) # 2초 단위 설정
    # 현재 폴더에 저장됨