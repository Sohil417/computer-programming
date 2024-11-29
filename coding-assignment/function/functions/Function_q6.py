# Define a function that squares all elements in a list
def square_elements(numbers):
    return [x**2 for x in numbers]

# Call the function
nums = [1, 2, 3, 4]
print(square_elements(nums))  # Output: [1, 4, 9, 16]
