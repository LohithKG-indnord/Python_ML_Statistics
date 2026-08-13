#Day : Wednesday

#List
colors = ["red", "green", "blue"]
print(colors[0])
colors[1] = "yellow"
colors.append("purple")
colors.remove("red")
print(colors)

#Tuples
fruits = ("apple", "banana", "cherry")
print(fruits[1])
print(len(fruits))
(a, b, c) = fruits
print(b)

#Sets
colors = {"red", "green", "blue"}
print(colors)
colors.add("yellow")
colors.discard("green")
print(len(colors))

#Dictionaries
car = {"brand": "Ford", "model": "Mustang", "year": 2024}
print(car["model"])
car["color"] = "red"
car.pop("brand")
print(car)