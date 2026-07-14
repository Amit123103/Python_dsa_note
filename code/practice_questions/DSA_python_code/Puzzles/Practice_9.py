'''9. Four Distinct Values Non-Consecutive

Write a Python program to find a list of integers containing exactly four distinct values, such that no integer repeats twice consecutively among the first twenty entries.
Input:
[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
Output:
True
Input:
[1, 2, 3, 3, 1, 2, 3, 3, 1, 2, 3, 3, 1, 2, 3, 3]
Output:
False
Input:
[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
Output:
False
'''


# Define a function named 'test' that takes a list of integers 'nums' as input
def test(nums):
    # Check if no integer in 'nums' repeats consecutively and if there are exactly four distinct values in 'nums'
    return all([nums[i] != nums[i + 1] for i in range(len(nums) - 1)]) and len(set(nums)) == 4

# Create a list of integers 'nums' with specific elements
nums = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]

# Print the original list
print("Original list:")
print(nums)

# Print a message indicating the condition being checked on the list
print("Check said list of integers containing exactly four distinct values, such that no integer repeats twice consecutively:")

# Print the result of the test function applied to the 'nums' list
print(test(nums))

# Create a different list of integers 'nums' with specific elements
nums = [1, 2, 3, 3, 1, 2, 3, 3, 1, 2, 3, 3, 1, 2, 3, 3]

# Print the original list
print("\nOriginal list:")
print(nums)

# Print a message indicating the condition being checked on the list
print("Check said list of integers containing exactly four distinct values, such that no integer repeats twice consecutively:")

# Print the result of the test function applied to the modified 'nums' list
print(test(nums))

# Create another list of integers 'nums' with specific elements
nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]

# Print the original list
print("\nOriginal list:")
print(nums)

# Print a message indicating the condition being checked on the list
print("Check said list of integers containing exactly four distinct values, such that no integer repeats twice consecutively:")

# Print the result of the test function applied to the modified 'nums' list
print(test(nums))
