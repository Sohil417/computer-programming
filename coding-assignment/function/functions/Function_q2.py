# Define a function that accepts a variable number of arguments
def sum_numbers(*args):
    return sum(args)

# Call the function with different numbers of arguments
print(sum_numbers(1, 2, 3))  # Output: 6
print(sum_numbers(5, 10))    # Output: 15
