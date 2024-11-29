numbers = [1, 2, 3, 4, 5, 6]

# Get numbers that are even and greater than 2
filtered = [x for x in numbers if x % 2 == 0 and x > 2]
print(filtered)  # Output: [4, 6]
