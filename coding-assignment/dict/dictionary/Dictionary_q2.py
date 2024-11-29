# Initial dictionary
student = {
    "name": "Alice",
    "age": 20,
    "courses": ["Math", "Science"]
}

# Add a new course
student["courses"].append("History")

# Update age
student["age"] = 21

# Remove a course
student["courses"].remove("Math")

# Check if a key exists
if "name" in student:
    print("Name exists:", student["name"])

# Iterate through key-value pairs
for key, value in student.items():
    print(f"{key}: {value}")
