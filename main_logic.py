import pyautogui as p
import asyncio as a
import threading
import time

img1 = []
img2 = []

start_x = 0
start_y = 0
end_x = 0
end_y = 0

def click_emoji(a,b,c,d,amt):
    global start_x,start_y, end_x,end_y
    start_x = a
    start_y = b
    end_x = c
    end_y = d
    t_move_mouse = threading.Thread(target=move_mouse, args=(start_x,start_y,end_x,end_y))
    t_find_heart = threading.Thread(target=find_heart,args=(t_move_mouse,))
    t_find_heart.daemon = True
    t_move_mouse.start()
    t_find_heart.start()


### move mouse
def move_mouse(start_x,start_y,end_x,end_y):
    p.moveTo(start_x,start_y)
    p.moveTo(start_x,end_y,duration=5)

### 하트 이미지 찾기
def find_heart(t_move_mouse):
    global img1
    print('find_heart is activating')
    while t_move_mouse.is_alive:
        print('t_move_mouse is activating : ', t_move_mouse.is_alive)
        time.sleep(1)
        while img1 is None:
            print('finding_image')
            img1.append(p.locateOnScreen('./img/heart.png',confidence=0.9))

### 감정이모티콘 찾기
def find_emotion(img1):
    global img2
    p.click(img1)
    while img2 is None:
        img2.append(p.locateOnScreen('./img/emotion2.png',confidence=0.9))
    return img2



t_find_emotion = threading.Thread(target=find_emotion)

