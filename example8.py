# Example 8: Create a new list from two list using the following condition.
# Given lists
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

# Create a new list with odd numbers from list1 and even numbers from list2
new_list = [num for num in list1 if num % 2 != 0] + [num for num in list2 if num % 2 == 0]

# Print the new list
print("New List:", new_list)