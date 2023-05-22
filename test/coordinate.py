import pyautogui as p
import threading as t
import time

coordinate = []
amt = 0

def save_coordinate():
    global coordinate,amt
    while p.position() != (100,500):
        img = p.locateOnScreen('./img/heart.png',confidence=0.9)
        if img is not None:
            coordinate.append(img)
        time.sleep(0.5)
        print(coordinate)

def daemon_test():
    while True:
        print('데몬스레드')
        time.sleep(0.3)
        

save_coordinate_thread = t.Thread(target=save_coordinate)

## 데몬 스레드 생성
daemon = t.Thread(target=daemon_test)

## 데몬 스레드 설정
daemon.daemon = True

save_coordinate_thread.start()

daemon.start()


while True:
    amt += 1
    print('메인스레드==========================',amt)
    p.moveTo(100,500,duration=5)
    time.sleep(1)
    if amt == 20:
        break



save_coordinate_thread.join()



