import os
import time
import random
i = 0
while True:
  time.sleep(10)
  i = i + 1
  os.system("cd ~/Desktop/ && echo YOU ARE DEAD > DEATH-" + str(i) + ".txt")
