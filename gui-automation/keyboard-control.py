import pyautogui

pyautogui.click(100, 100); pyautogui.typewrite('Hello world!')

pyautogui.click(100, 100); pyautogui.typewrite('Hello world!', interval=0.2)

pyautogui.click(100, 100); pyautogui.typewrite(['a', 'b', 'left', 'left', 'X', 'Y'], inverval=1) # prints XYab

print(pyautogui.KEYBOARD_KEYS) # list keyboard keys

pyautogui.press('f1')

pyautogui.hotkey('ctrl', 'o')