import pyautogui
import time
import random
while True:
  time.sleep(random.randint(1, 20))
  pyautogui.click(random.randint(1, 100), random.randint(1, 100))
