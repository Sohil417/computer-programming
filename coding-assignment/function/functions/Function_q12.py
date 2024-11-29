# Define a function to check if a number is within a range and even
def check_range_and_even(num):
    if num >= 1 and num <= 10 and num % 2 == 0:
        return "In range and even"
    elif num >= 1 and num <= 10:
        return "In range but not even"
    else:
        return "Out of range"

# Test the function
print(check_range_and_even(4))  # Output: In range and even
print(check_range_and_even(7))  # Output: In range but not even
print(check_range_and_even(15)) # Output: Out of range
