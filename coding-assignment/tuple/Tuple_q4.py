# Creating a Tuple
tuple1 = (10, 20, 30, 40, 50)

# Accessing elements from the tuple using indexing
print("Accessing elements using indexing:")
print("First element:", tuple1[0])     # Output: 10
print("Last element:", tuple1[-1])     # Output: 50
print("Third element:", tuple1[2])     # Output: 30

# Slicing a Tuple (extracting a portion of the tuple)
print("\nSlicing the tuple:")
sliced_tuple = tuple1[1:4]  # Getting elements from index 1 to 3
print("Sliced tuple:", sliced_tuple)  # Output: (20, 30, 40)

# Concatenating tuples
tuple2 = (60, 70)
concatenated_tuple = tuple1 + tuple2
print("\nConcatenated tuple:")
print(concatenated_tuple)  # Output: (10, 20, 30, 40, 50, 60, 70)

# Repeating a tuple (multiplying a tuple)
repeated_tuple = tuple2 * 3
print("\nRepeated tuple:")
print(repeated_tuple)  # Output: (60, 70, 60, 70, 60, 70)

# Tuple Length (Number of elements)
print("\nLength of tuple1:")
print(len(tuple1))  # Output: 5

# Nested Tuple (tuple inside a tuple)
nested_tuple = (1, 2, (3, 4, 5), 6)
print("\nNested tuple:")
print("Element at index 2:", nested_tuple[2])  # Output: (3, 4, 5)
print("Element inside nested tuple:", nested_tuple[2][1])  # Output: 4

# Tuple Unpacking
print("\nTuple Unpacking:")
a, b, c, d, e = tuple1
print("Unpacked values:")
print(f"a: {a}, b: {b}, c: {c}, d: {d}, e: {e}")

# Using Tuple Methods - count and index
print("\nUsing tuple methods:")
tuple3 = (10, 20, 10, 30, 10)
print("Count of 10 in tuple3:", tuple3.count(10))  # Output: 3
print("Index of 30 in tuple3:", tuple3.index(30))  # Output: 3

# Checking if an element exists in a tuple
print("\nChecking if an element exists in tuple1:")
print(30 in tuple1)  # Output: True
print(60 in tuple1)  # Output: False
