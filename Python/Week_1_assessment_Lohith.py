# Q1. Write a script that takes a number and prints whether it's positive, negative, or zero, and whether it's even or odd.

n = int(input("Enter a number:"))

if n % 2 == 0:
    print("Given number is Even")
else: 
    print("The given number is Odd")

if n > 0:
    print(f"The given number {n} is: Positive")
elif n==0:
    print(f"The fiven number {n} is: zero")
else:
    print(f"The given number {n} is: negative")

# Q2. Write a function that takes a sentence and returns the count of vowels and the sentence reversed, using a loop.

def vowels(sentence):
    rev = ''
    vow = ['a','e','i','o','u']
    count = 0
    for x in sentence:
        if x in vow:
            count += 1
    return count
    

n = input()
print(vowels(n))


#Q3. Given a list of student names and marks, build a dictionary from them, then use a comprehension to get all students scoring above 50.
names = ['rohit','vijay','sumit']
marks = [45 , 76 , 89]


mydict = {
    names : 'names',
    marks : 'marks'
}

x = [x  for x in mydict if x > 50]
print(x)



# Q4. Write a script that reads a text file and prints its line count — handle the file-not-found case gracefully with try/except.

try:
    with open("data.txt") as f:
        for x in f:
            print(x)
except:
    print("The file does not exist")


# Q5. Write a function with default arguments and *args that calculates the average of any number of values, with input validation.

def my_func(*num):
    for i in range(len(num)):
        pass
my_func(num)