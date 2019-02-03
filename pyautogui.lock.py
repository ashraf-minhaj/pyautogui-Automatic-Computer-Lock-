"""
Seek user permission before locking the pc.
Version2 of pyautogui.lock.py Code.
by Ashraf Minhaj.
find me at ashraf_minhaj@yahoo.com
tutorial- ashrafminhajfb.blogspot.com
"""

"""
Change the sleep(time) / delay time as per your system.
It is set so that the code doesn't run faster than the 
Computer system
"""
import pyautogui   #import pyautogui 
from time import sleep  #import sleep

#seek user permisssion before locking
x = pyautogui.confirm("Do you want to lock the screen?") 

#check if user clicked Ok or Cancel
if x == "OK":               #if User pressed OK
    print("locking the pc")

    #execute locking code
    pyautogui.hotkey('win', 'r')  #type win+r (run) combo key
    sleep(0.01)  #a bit delay
    pyautogui.typewrite("cmd\n") #write cmd(command prompt) '\n' for 'ENTER' command
    sleep(0.500)  #delay so that the code doesn't run faster than the compluter
    pyautogui.typewrite("rundll32.exe user32.dll, LockWorkStation\n") #type and hit 'ENTER' in the command prompt
 
if x == "Cancel":  #if Cancel do nothing
    print("screen lock cancelled")
