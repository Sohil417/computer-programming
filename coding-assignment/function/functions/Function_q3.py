# Define a function that accepts a variable number of keyword arguments
def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Call the function with keyword arguments
display_info(name="Alice", age=25, city="New York")
# Output:
# name: Alice
# age: 25
# city: New York
