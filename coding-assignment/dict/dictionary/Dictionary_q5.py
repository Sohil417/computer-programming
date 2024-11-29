# Create a dictionary
student = {
    "name": "Alice",
    "age": 20,
    "courses": ["Math", "Science"]
}

# 1. Print the original dictionary
print("Original dictionary:")
print(student)

# 2. Add a new key-value pair
student["city"] = "New York"
print("\nAfter adding city:")
print(student)

# 3. Update an existing value
student["age"] = 21
print("\nAfter updating age:")
print(student)

# 4. Remove a key-value pair using pop()
removed_course = student.pop("courses")
print("\nAfter removing courses:")
print(student)
print(f"Removed value (courses): {removed_course}")

# 5. Remove a key-value pair using del
del student["city"]
print("\nAfter deleting 'city' key:")
print(student)

# 6. Check if a key exists in the dictionary
if "name" in student:
    print("\nThe key 'name' exists in the dictionary.")

# 7. Iterate through the dictionary keys
print("\nIterating through dictionary keys:")
for key in student:
    print(key)

# 8. Iterate through the dictionary values
print("\nIterating through dictionary values:")
for value in student.values():
    print(value)

# 9. Iterate through key-value pairs
print("\nIterating through key-value pairs:")
for key, value in student.items():
    print(f"{key}: {value}")

# 10. Using get() method (safe retrieval of values)
age = student.get("age", "Not Found")
print(f"\nUsing get() to retrieve age: {age}")

# 11. Copy the dictionary using copy()
student_copy = student.copy()
print("\nAfter copying the dictionary:")
print(student_copy)

# 12. Merging two dictionaries
new_info = {"email": "alice@example.com", "phone": "123-456-7890"}
student.update(new_info)
print("\nAfter merging with new information:")
print(student)

# 13. Using dictionary comprehension
squares = {x: x**2 for x in range(5)}
print("\nDictionary comprehension (squares):")
print(squares)
