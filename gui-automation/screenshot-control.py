import pyautogui

pyautogui.screenshot('c:\\screenshot_example.png')

# must be pixel perfect
pyautogui.locateOnScreen('c:\\calc7key.png')

# must be pixel perfect
pyautogui.locateCenterOnScreen('c:\\calc7key.png') # returns (932, 336)

pyautogui.moveTo((932, 336), duration=1)
pyautogui.click(932, 336)