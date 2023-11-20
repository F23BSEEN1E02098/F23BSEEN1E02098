# Example 7: Check Palindrome Number
# Given number
number = 121

# Convert the number to a string for easy reversal
num = str(number)

# Reverse the string
reversed_str = num[::-1]

# Check if the original and reversed strings are the same
if num == reversed_str:
    print(f"{number} is a palindrome number.")
else:
    print(f"{number} is not a palindrome number.")