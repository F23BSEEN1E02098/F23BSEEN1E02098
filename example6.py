# Example 6:  Print the following pattern
# 1
# 22
# 333
# 4444
# 55555

# Number of rows in the pattern
num_rows = 5

# Iterate to print the pattern
for i in range(1, num_rows + 1):
    # Inner loop to print repeated numbers
    for j in range(i):
        print(i, end="")
    # Move to the next line after each row
    print()