import pyautogui
import time


x=1
while x<4:
   pyautogui.screenshot('/home/zach/tensorflow1/models/research/object_detection/utils/'+str(x)+'.png')
   x+=1
   time.sleep(20)
