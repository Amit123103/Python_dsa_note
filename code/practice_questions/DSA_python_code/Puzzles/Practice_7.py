'''7. Sum of First i Equals i

Write a Python program to check a given list of integers where the sum of the first i integers is i.
Input:
[0, 1, 2, 3, 4, 5]
Output:
False
Input:
[1, 1, 1, 1, 1, 1]
Output:
True
Input:
[2, 2, 2, 2, 2]
Output:
False
'''
# Define a function named 'test' that takes a list 'li' and an integer 'i' as input
def test(li, i):
    # Check if the sum of the first 'i' integers in 'li' equals 'i'
    return sum(li[:i]) == i

# Create a list 'nums' with specific elements
nums = [0, 1, 2, 3, 4, 5]

# Assign an integer 'i' to the variable
i = 1

# Print the original list
print("Original list:")
print(nums)

# Print a message indicating the current value of 'i'
print("Check the said list, where the sum of the first i integers is i: i =", i)

# Print the result of the test function applied to the 'nums' list with the current value of 'i'
print(test(nums, 1))

# Update the value of 'i'
i = 3

# Print a message indicating the updated value of 'i'
print("\nOriginal list:")
print(nums)

# Print the result of the test function applied to the 'nums' list with the updated value of 'i'
print("Check the said list, where the sum of the first i integers is i: i =", i)
print(test(nums, 3))

# Update the value of 'i' and 'nums'
i = 6
nums = [1, 1, 1, 1, 1, 1]

# Print a message indicating the updated value of 'i'
print("\nOriginal list:")
print(nums)

# Print the result of the test function applied to the updated 'nums' list with the updated value of 'i'
print("Check the said list, where the sum of the first i integers is i: i =", i)
print(test(nums, 6))

# Update the value of 'i' and 'nums'
i = 2
nums = [2, 2, 2, 2, 2]

# Print a message indicating the updated value of 'i'
print("\nOriginal list:")
print(nums)

# Print the result of the test function applied to the updated 'nums' list with the updated value of 'i'
print("Check the said list, where the sum of the first i integers is i: i =", i)
print(test(nums, 2))
