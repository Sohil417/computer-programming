# Define a function to check if both 'apple' and 'banana' are in the list
def check_fruits(fruit_list):
    if 'apple' in fruit_list and 'banana' in fruit_list:
        return "Both apple and banana are in the list"
    else:
        return "Either apple or banana is not in the list"

# Test the function
print(check_fruits(["apple", "banana", "cherry"]))  # Output: Both apple and banana are in the list
print(check_fruits(["apple", "cherry"]))             # Output: Either apple or banana is not in the list
