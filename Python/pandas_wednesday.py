import pandas as pd

df = pd.read_csv("data.csv")

# Viewing the data
print(df.to_string())

# Getting information about the data
print(df.info())

# Getting statistical information
print(df.describe())

# Cleaning empty cells
df = df.dropna()

print(df.to_string())

# Filling empty cells
df = pd.read_csv("data.csv")

df["Calories"] = df["Calories"].fillna(130)

print(df.to_string())

# Removing duplicates
df = pd.read_csv("data.csv")

df.drop_duplicates(inplace=True)

print(df.to_string())

# Finding correlations
df = pd.read_csv("data.csv")

print(df.corr())

# Plotting the data
import matplotlib.pyplot as plt

df.plot()
plt.show()

# Scatter plot
df.plot(
    kind="scatter",
    x="Duration",
    y="Calories"
)

plt.show()

# Histogram
df["Duration"].plot(kind="hist")

plt.show()