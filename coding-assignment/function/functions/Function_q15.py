# Define a function that checks if a number is even and divisible by 5
def check_even_and_divisible_by_five(num):
    if num % 2 == 0 and num % 5 == 0:  # If num is even and divisible by 5
        return True
    else:
        return False

# Test the function
print(check_even_and_divisible_by_five(10))  # Output: True
print(check_even_and_divisible_by_five(7))   # Output: False
