import pyautogui as p
import threading as t
import time

img1 = []

def move_mouse():
    p.moveTo(500,500,duration=2)

def find_heart():
    while True:
        print(1111)
        time.sleep(0.3)
        img1.append('./img/heart.png')

find_heart_thread = t.Thread(target=find_heart)
find_heart_thread.daemon = True
find_heart_thread.start()

move_mouse()