import pyautogui
import time



def print_screen():
 x=1
 while(x<4):
  pyautogui.screenshot('Specify path of folder you want to save photo'+str(x)+'.png')
  x+=1
  time.sleep(0)
