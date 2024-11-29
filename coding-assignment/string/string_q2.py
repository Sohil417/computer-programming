# Checking if a string is a palindrome:
n=str(input("enter the number: "))
nn=n[::-1]
if nn==n:
    print("palindrome")
else:
    print("not palindrome")