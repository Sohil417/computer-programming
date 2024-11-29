# Define a function to check if a person is eligible to vote
def check_voting_eligibility(age, citizenship):
    if age >= 18 and citizenship == "US":
        return "Eligible to vote"
    else:
        return "Not eligible to vote"

# Test the function
print(check_voting_eligibility(20, "US"))  # Output: Eligible to vote
print(check_voting_eligibility(17, "US"))  # Output: Not eligible to vote
print(check_voting_eligibility(20, "Canada"))  # Output: Not eligible to vote
