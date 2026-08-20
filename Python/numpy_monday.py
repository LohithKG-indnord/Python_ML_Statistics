import numpy as np

# Creating an array
a = np.array([10, 20, 30, 40, 50])
print("Array:", a)

# Creating a 2D array
b = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\n", b)

# Checking array properties
print("Dimensions:", b.ndim)
print("Shape:", b.shape)
print("Data type:", a.dtype)

# Indexing
print("First element:", a[0])
print("Last element:", a[-1])
print("Element from 2D array:", b[1, 2])

# Slicing
print("First 3 elements:", a[:3])
print("Every second element:", a[::2])

# Reshaping
c = np.array([1, 2, 3, 4, 5, 6])
c = c.reshape(2, 3)
print("Reshaped array:\n", c)

# Sorting
d = np.array([5, 2, 8, 1, 3])
print("Sorted array:", np.sort(d))

# Filtering
print("Values greater than 25:", a[a > 25])

# Joining arrays
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
print("Joined array:", np.concatenate((x, y)))

# Basic calculations
print("Sum:", np.sum(a))
print("Mean:", np.mean(a))
print("Maximum:", np.max(a))
print("Minimum:", np.min(a))
print("Standard deviation:", np.std(a))

# Random numbers
random_num = np.random.randint(1, 100, 5)
print("Random numbers:", random_num)

# Normal distribution
normal = np.random.normal(50, 10, 5)
print("Normal distribution:", normal)

# Mathematical functions
numbers = np.array([1, 4, 9, 16])
print("Square root:", np.sqrt(numbers))
print("Log:", np.log(numbers))

# Trigonometric functions
angles = np.array([0, np.pi / 2, np.pi])
print("Sine:", np.sin(angles))
print("Cosine:", np.cos(angles))