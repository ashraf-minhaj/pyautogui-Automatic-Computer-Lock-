"""
pyautogui automatic pc lock code.
by Ashraf Minhaj.
find me- ashraf_minhaj@yahoo.com
"""

import pyautogui  #import pyautogui library
from time import sleep  #import sleep - for the delay

pyautogui.hotkey('win', 'r') #windows_key + Run 

pyautogui.typewrite("cmd\n")  #cmd to open command prompt
sleep(0.500)      #500 milisec delay
#write the code then press enter('\n') thus pc will auto-lock
pyautogui.typewrite("rundll32.exe user32.dll, LockWorkStation\n") 
