my_list = ["apple", "banana", "cherry"]

# Remove by value
my_list.remove("banana")
print(my_list)  # Output: ['apple', 'cherry']


# Pop an element (removes last by default)
last_item = my_list.pop()
print(last_item)  # Output: cherry
print(my_list)    # Output: []
