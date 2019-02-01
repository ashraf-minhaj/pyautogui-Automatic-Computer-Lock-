import pyautogui
from time import sleep

pyautogui.hotkey('win', 'r')

pyautogui.typewrite("cmd\n")
sleep(0.500)
pyautogui.typewrite("rundll32.exe user32.dll, LockWorkStation\n")