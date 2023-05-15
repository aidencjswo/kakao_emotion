import pyautogui
import tkinter as tk
import time


window = tk.Tk()
window.geometry('600x600')
window.resizable(False,False)
window.title('Kakao-Emotion')
##############################
#val-area-start!!
##############################
start_mouse_x = 0
start_mouse_y = 0


##############################
#def-area-start!!
##############################
def start_mouse_position_def():
    global start_mouse_x, start_mouse_y
    time.sleep(2)
    start_mouse_x, start_mouse_y = pyautogui.position()

def check_start_mouse_position():
    pyautogui.moveTo(start_mouse_x,start_mouse_y,duration=0.5)

def find_img1():
    img1 = pyautogui.locateOnScreen('./img/heart.png')
    print(img1)
##############################
#mainloop() start!!
##############################

###
start_mouse_position_description_label = tk.Label(window,text='start_mouse_position')
start_mouse_position_description_label.pack()
start_mouse_position_description_button = tk.Button(window,text='CLICK!!',command=start_mouse_position_def)
start_mouse_position_description_button.pack()
###

###
check_start_mouse_position_label = tk.Label(window,text='check_start_mouse_position')
check_start_mouse_position_label.pack()
check_start_mouse_position_button = tk.Button(window,text="CHECK!",command=check_start_mouse_position)
check_start_mouse_position_button.pack()
###

search_img1_label = tk.Label(text='find_first_image')
search_img1_label.pack()
search_img1_button = tk.Button(text='CLICK',command=find_img1)
search_img1_button.pack()

##############################
window.mainloop()