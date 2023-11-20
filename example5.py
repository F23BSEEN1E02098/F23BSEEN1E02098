# Example 5:Display numbers divisible by 5 from a list. 
# Given list of numbers
g_list = [10, 20, 33, 46, 55]

# Iterate and print numbers divisible by 5
print("Numbers divisible by 5:")
for num in g_list:
    if num % 5 == 0:
        print(num)