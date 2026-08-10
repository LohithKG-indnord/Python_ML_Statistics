#Day : Monday


#Variables
x = 5
y = "john"
print(type(x))

#Data Types
x = 5
y = 3.14
z = "Hello"
print(type(x))
print(type(y))
print(type(z))

#Operators
a = 15
b = 4
print(a%b)
print(a//b)
print(a**b)
a += 10

#If-Else
age = 20
if age < 13:
  print("Child")
elif age < 18:
  print("Teenager")
else:
  print("Adult")

#Match
day = 3
match day:
  case 3:
    print("Wednesday")
  case _:
    print("Other day")