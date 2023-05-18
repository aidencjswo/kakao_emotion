import pyautogui as p
import threading


img1 = 0
img2 = 0

def function_1():
    global img1
    for i in range(30):
        img1 = p.locateOnScreen('./img/heart.png', confidence=0.8)
        if img1 is not None:
            global img2
            img2 = p.locateOnScreen('./img/emotion2.png',confidence=0.9)
            print(img2)
            p.click(img1)
            p.click(img2)

            

def function_2():
    p.moveTo(500,1000)
    p.moveTo(500,0,duration=7)

function_1_thread = threading.Thread(target=function_1)
function_2_thread = threading.Thread(target=function_2)
function_1_thread.start()
function_2_thread.start()

function_2_thread.join()

