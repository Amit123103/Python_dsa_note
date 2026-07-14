'''Sum of Series n + (n-2) + (n-4) ... Using Recursion

Write a Python program to calculate the sum of the positive integers of n+(n-2)+(n-4)... (until n-x =< 0) using recursion .

Test Data:
sum_series(6) -> 12
sum_series(10) -> 30
'''
# def sum_series(num):
#     if num < 1:
#         return 0
#     else:
#         return num + sum_series(num -2)
# print(sum_series(6))

# print(sum_series(10))


# Define a function named sum_series that calculates the sum of a series of numbers
def sum_series(n):
    # Check if 'n' is less than 1 (base case for the series)
    if n < 1:
        # If 'n' is less than 1, return 0 (base case value for the sum)
        return 0
    else:
        # If 'n' is greater than or equal to 1, calculate the sum of 'n' and
        # recursively call the sum_series function with 'n - 2'
        return n + sum_series(n - 2)

# Print the result of calling the sum_series function with the input value 6
print(sum_series(6))

# Print the result of calling the sum_series function with the input value 10
print(sum_series(10))
