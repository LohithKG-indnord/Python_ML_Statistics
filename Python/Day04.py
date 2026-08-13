#Day : Thursday

#Exception Handling
x = "Hello"
try:
  print(x)
except:
  print("An error occurred")
finally:
  print("Execution complete")

#File Handling
f = open("demofile.txt")
print(f.read())

with open("demofile.txt", "a") as f:
  f.write("Now the file has more content!")

with open("demofile.txt") as f:
  print(f.read())

f.close()

#Deleting
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")