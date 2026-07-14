''' Sum of Digits of an Integer Using Recursion

Write a Python program to get the sum of a non-negative integer using recursion.

Test Data:
sumDigits(345) -> 12
sumDigits(45) -> 9
'''
# def digit_sum(num):
#     if num == 0:
#         return 0
#     else:
#         return num % 10 + digit_sum(int(num / 10))
    
    
# print(digit_sum(45))
    
    
# Define a function named sumDigits that calculates the sum of the digits of a given number 'n'
def sumDigits(n):
    # Check if 'n' is 0 (base case for summing digits)
    if n == 0:
        # If 'n' is 0, return 0 (no digits to sum)
        return 0
    else:
        # If 'n' is not 0, calculate the sum of the last digit (n % 10) and
        # recursively call the sumDigits function on the remaining digits (n / 10)
        return n % 10 + sumDigits(int(n / 10))

# Print the result of calling the sumDigits function with the input value 345
print(sumDigits(345))

# Print the result of calling the sumDigits function with the input value 45
print(sumDigits(45))
