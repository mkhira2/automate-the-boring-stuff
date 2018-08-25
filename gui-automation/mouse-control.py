import pyautogui

# FAILSAFE: move mouse to upper-left corner of screen (0, 0)

print(pyautogui.size()) 
width, height = pyautogui.size()

print(pyautogui.position())

pyautogui.moveTo(100, 100)
pyautogui.moveTo(100, 100, duration = 1.5)

pyautogui.moveRel(200, 0)
pyautogui.moveRel(200, 0, duration=2)

# click, doubleClick, middleClick, rightClick
pyautogui.click(339, 38)

print(pyautogui.displayMousePosition())

# draws spirals in MS paint
pyautogui.click()
distance = 200
while distance > 0:
    print(distance, 0)
    pyautogui.dragRel(distance, 0, duration=0.1) # move right
    distance = distance - 25
    print(0, distance)
    pyautogui.dragRel(0, distance, duration=0.1) # move down
    print(-distance, 0)
    pyautogui.dragRel(-distance, 0, duration=0.1) # move left
    distance = distance - 25
    print(0, distance)
    pyautogui.dragRel(0, -distance, duration=0.1) # move up