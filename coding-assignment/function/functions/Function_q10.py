# Define a function to check if a number is positive and even
def check_number(num):
    if num > 0 and num % 2 == 0:
        return "Positive and Even"
    elif num > 0 and num % 2 != 0:
        return "Positive and Odd"
    else:
        return "Not Positive"

# Test the function
print(check_number(4))  # Output: Positive and Even
print(check_number(3))  # Output: Positive and Odd
print(check_number(-2)) # Output: Not Positive
