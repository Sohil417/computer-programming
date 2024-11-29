# Using Tuple Methods - count and index
tuple1 = (10, 20, 30, 40, 50)

print("\nUsing tuple methods:")
tuple3 = (10, 20, 10, 30, 10)
print("Count of 10 in tuple3:", tuple3.count(10))  # Output: 3
print("Index of 30 in tuple3:", tuple3.index(30))  # Output: 3

# Checking if an element exists in a tuple
print("\nChecking if an element exists in tuple1:")
print(30 in tuple1)  # Output: True
print(60 in tuple1)  # Output: False
