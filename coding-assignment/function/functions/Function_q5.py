# Define a function that checks if a number is positive, negative, or zero
def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

# Call the function
print(check_number(10))  # Output: Positive
print(check_number(-5))  # Output: Negative
print(check_number(0))   # Output: Zero
