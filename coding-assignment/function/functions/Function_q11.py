# Define a function that checks if two numbers are positive and their sum is even
def check_sum_positive_and_even(num1, num2):
    if num1 > 0 and num2 > 0 and (num1 + num2) % 2 == 0:
        return "Both numbers are positive and their sum is even"
    else:
        return "Either one or both numbers are not positive, or their sum is not even"

# Test the function
print(check_sum_positive_and_even(3, 5))  # Output: Both numbers are positive and their sum is even
print(check_sum_positive_and_even(-3, 5)) # Output: Either one or both numbers are not positive, or their sum is not even
