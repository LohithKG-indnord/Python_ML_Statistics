#Tuesday

#while loops
i = 0

while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

#For loops
fruits = ["apple", "banana", "cherry"]

for x in fruits:
  print(x)
  if x == "banana":
    break

#Functions
def greet(name):
  print("Hello, " + name)

greet("Emil")

#String 
txt = "Hello, World!"

print(txt[2:5])
print(txt.upper())
name = "Python"
print(f"I love {name}")