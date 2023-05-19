import pyautogui as p
import threading as t
import time

coordinate = []

def save_coordinate():
    global coordinate
    while p.position() != (100,500):
        img = p.locateOnScreen('./img/heart.png',confidence=0.9)
        if img is not None:
            coordinate.append(img)
        time.sleep(0.5)
        print(coordinate)
        

save_coordinate_thread = t.Thread(target=save_coordinate)


save_coordinate_thread.start()

p.moveTo(100,500,duration=5)

save_coordinate_thread.join()


