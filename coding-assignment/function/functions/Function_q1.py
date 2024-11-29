# Define a function with a default argument value
def greet(name="Guest"):
    print(f"Hello, {name}!")

# Call the function with and without an argument
greet("Alice")  # Output: Hello, Alice!
greet()         # Output: Hello, Guest!
