# Example 9: Print a downward Half-Pyramid Pattern of Star (asterisk)

# Number of rows in the pattern
x = 5

# Iterate to print the downward half-pyramid pattern
for i in range(x, 0, -1):
    for j in range(i):
        print('*', end=' ')
    print()