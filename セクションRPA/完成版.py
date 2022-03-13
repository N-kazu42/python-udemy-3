#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pyautogui
import pyperclip
import time

pyautogui.hotkey("win","d")
pyautogui.doubleClick(1703,721)
time.sleep(1)
x,y=pyautogui.locateCenterOnScreen("icon.PNG")
pyautogui.doubleClick(x,y)
time.sleep(1)
pyautogui.click(x=788,y=301)
pyperclip.copy("テスト")
pyautogui.hotkey("ctrl","v")
time.sleep(1)
pyautogui.hotkey("ctrl","s")
time.sleep(1)
pyautogui.hotkey("ctrl","w")
time.sleep(1)

print("終了しました")

