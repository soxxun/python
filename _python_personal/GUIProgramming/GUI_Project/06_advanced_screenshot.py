
# 사용자 지정 키값으로 설정된 동작 실행시키기 --> Hooking

import time
import keyboard
from PIL import ImageGrab


def screenshot():
    # 2022년 4월 28일 17시 20분 30초 --> '_20220428_172030'
    curr_time = time.strftime('_%Y%m%d_%H%M%S')
    img = ImageGrab.grab()
    img.save(f'image{curr_time}.png') # 'image_20220428_172030'

# 사용 방법 --> add_hotkey
keyboard.add_hotkey('F9', screenshot) # 사용자가 F9키를 누르면 screenshot 저장
# 단일키, 복합키 모두 가능 (ex. 'a' or 'Ctrl_shift+s', etc)

keyboard.wait('esc') # esc 키를 누를 때까지 프로그램 수행

# mission complete ~ !!!!!