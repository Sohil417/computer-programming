my_list = [10, 20, 30, 40]

# Check if all numbers are greater than 5 and less than 50
if all(x > 5 and x < 50 for x in my_list):
    print("All elements are between 5 and 50.")
else:
    print("Some elements are outside the range.")
