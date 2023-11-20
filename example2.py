# Example 2:Print the sum of the current number and the previous number.
for i in range(1, 11):
    # Calculate the sum of the current and previous numbers
    current_number = i
    previous_number = i - 1 if i > 1 else 0
    sum_of_numbers = current_number + previous_number

    # Print the result for each iteration
    print(f"Iteration {i}: Sum of {current_number} and {previous_number} is {sum_of_numbers}")