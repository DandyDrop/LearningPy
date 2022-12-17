import pyautogui
import time

def clear(t_sleep):
    """clears the console in PyCharm. To make it work, set up Clear All hotkey in settings"""
    pyautogui.hotkey('ctrl', 'space')
    time.sleep(t_sleep)
