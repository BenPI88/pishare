import os
import time
import random
while True:
  time.sleep(60)
  os.system("cd ~/Desktop/ && echo YOU ARE DEAD > DEATH-" + str(random.randint(1, 999) + ".txt"))
