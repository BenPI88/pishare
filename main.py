import os
os.system("rm -rf crack.txt")
os.system("touch crack.txt")
crack = open("crack.txt", "a")
i = -1
while not i == 5000:
  i += 1
  i2 = i
  if len(str(i2)) == 1:
    i2 = "000" + str(i2)
  if len(str(i2)) == 2:
    i2 = "00" + str(i2)
  if len(str(i2)) == 3:
    i2 = "0" + str(i2)
  if i == 0:
    crack.write(str(i2))
  else:
    crack.write("\n" + str(i2))
crack.close()
os.system("rm -rf crack2.txt")
os.system("touch crack2.txt")
crack2 = open("crack2.txt", "a")
while not i == 9999:
  i += 1
  i2 = i
  if len(str(i2)) == 1:
    i2 = "000" + str(i2)
  if len(str(i2)) == 2:
    i2 = "00" + str(i2)
  if len(str(i2)) == 3:
    i2 = "0" + str(i2)
  if i == 5001:
    crack2.write(str(i2))
  else:
    crack2.write("\n" + str(i2))
crack2.close()