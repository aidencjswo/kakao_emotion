import pyautogui as p

def click_emoji(x,y,img1, img2):
    print(x,y)
    p.moveTo(x,y)
    p.moveTo(img1)
    p.click()
