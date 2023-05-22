import pyautogui as p
import asyncio as a
import threading
import time
from launch import start_mouse_x as aa,start_mouse_y as bb

print(aa,bb)

img1 = []
img2 = []

### 마우스이동하기 - sub thread
def move_mouse(start_x,start_y,end_x,end_y,amt):
    # find_heart_thread.start()
    p.moveTo(start_x,start_y)
    p.moveTo(start_x,end_y,duration=5)

### 하트 이미지 찾기 - daemon thread
def find_heart():
    global img1
    while True:
        print('11111')
        time.sleep(0.3)
    img1.append(p.locateOnScreen('./img/heart.png'))
    print('find_heart is activating')
    
### 감정이모티콘 찾기 - daemon thread
def find_emotion(img1):
    p.click(img1)
    while img2 is None:
        img2.append(p.locateOnScreen('./img/emotion2.png',confidence=0.9))
    return img2

move_mouse_thread = threading.Thread(target=move_mouse)

find_heart_thread = threading.Thread(target=find_heart)
find_heart_thread.daemon=True