'''1. Check Nineteen and Five Occurrences

Write a Python program to find a list of integers with exactly two occurrences of nineteen and at least three occurrences of five. Return True otherwise False.
Input:
[19, 19, 15, 5, 3, 5, 5, 2]
Output:
True
Input:
[19, 15, 15, 5, 3, 3, 5, 2]
Output:
False
Input:
[19, 19, 5, 5, 5, 5, 5]
Output:
True
'''

# Define a function named 'test' that takes a list 'nums' as input
def test(nums):
    # Check if the count of 19 in 'nums' is equal to 2 and the count of 5 is greater than or equal to 3
    return nums.count(19) == 2 and nums.count(5) >= 3

# Create a list 'nums' with specific elements
nums = [19, 19, 15, 5, 3, 5, 5, 2]

# Print the original list
print("Original list:")
print(nums)

# Print the result of the test function applied to the 'nums' list
print("Check two occurrences of nineteen and at least three occurrences of five in the said list:")
print(test(nums))

# Create a different list 'nums' with specific elements
nums = [19, 15, 15, 5, 3, 3, 5, 2]

# Print the original list
print("\nOriginal list:")
print(nums)

# Print the result of the test function applied to the modified 'nums' list
print("Check two occurrences of nineteen and at least three occurrences of five in the said list:")
print(test(nums))

# Create another list 'nums' with specific elements
nums = [19, 19, 5, 5, 5, 5, 5]

# Print the original list
print("\nOriginal list:")
print(nums)

# Print the result of the test function applied to the modified 'nums' list
print("Check two occurrences of nineteen and at least three occurrences of five in the said list:")
print(test(nums))

