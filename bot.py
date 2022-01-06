from pyautogui import*
import pyautogui
import time
import keyboard
import random
import win32api,win32con

#Tile 1: X:  532 Y: 400 RGB: (156, 162, 230)
#tile 2 X:  716 Y: 400 RGB: (154, 160, 230)
#tile 3 X:  848 Y: 400 RGB: (253,  18,   1)
#tile 4 X: 1094 Y: 400 RGB: (167, 171, 233)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)#click  sometimes fail to execute if you click  too fast
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
while keyboard.is_pressed('q')==False:
    if(pyautogui.pixel(529,707)[0]==0):
       click(529,707)
    if(pyautogui.pixel(725,682)[0]==0):
       click(725,682)
    if(pyautogui.pixel(951,714)[0]==0):
       click(951,714)
    if(pyautogui.pixel(1071,676)[0]==0):
       click(1071,676)
