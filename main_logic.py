import pyautogui as p
import asyncio as a

img1 = None
img2 = None

def click_emoji(x,y):
    p.moveTo(x,y)
    p.moveTo(x,100,duration=1)
    img1 = find_heart()
    img2 = find_emotion(img1)
    p.click(img2)
    p.moveTo(x,y)

def find_heart():
    global img1
    while img1 is None:
        img1 = p.locateOnScreen('./img/heart.png',confidence=0.9)
    return img1

def find_emotion(img1):
    global img2
    p.click(img1)
    while img2 is None:
        img2 = p.locateOnScreen('./img/emotion2.png',confidence=0.9)
    return img2