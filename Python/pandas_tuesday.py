import pandas as pd

# Checking Pandas version
print(pd.__version__)

# Creating a Pandas Series
a = [1, 7, 2]
myvar = pd.Series(a)

print(myvar)

# Creating a Series with named indexes
myvar = pd.Series(a, index=["x", "y", "z"])

print(myvar)

# Creating a Series from a dictionary
calories = {
    "day1": 420,
    "day2": 380,
    "day3": 390
}

myvar = pd.Series(calories)

print(myvar)

# Creating a DataFrame
data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

df = pd.DataFrame(data)

print(df)

# Using named indexes
df = pd.DataFrame(
    data,
    index=["day1", "day2", "day3"]
)

print(df)

# Locating rows
print(df.loc["day2"])

# Loading CSV data
df = pd.read_csv("data.csv")

print(df)

# Printing the complete DataFrame
print(df.to_string())

# Viewing first rows
print(df.head())

# Viewing last rows
print(df.tail())

# Getting information about the DataFrame
print(df.info())