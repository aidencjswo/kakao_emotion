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
##############################
#mainloop() start!!
##############################


start_mouse_position_description = tk.Label(window,text='start_mouse_position')
start_mouse_position_description.pack()

start_mouse_position_description = tk.Button(window,text='CLICK!!',command=start_mouse_position_def)
start_mouse_position_description.pack()

check_start_mouse_position = tk.Button(window,text="CHECK!",command=check_start_mouse_position)
check_start_mouse_position.pack()

print('test')

##############################
window.mainloop()