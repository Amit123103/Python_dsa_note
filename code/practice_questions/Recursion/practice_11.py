''' Exponentiation Using Recursion

Write a Python program to calculate the value of 'a' to the power of 'b' using recursion.

Test Data :
(power(3,4) -> 81'''

# def calculate(a, b):
    
#     if b == 0:
#         return 1
#     elif a == 0:
#         return 0
#     elif b == 1:
#         return a
#     else:
#         return a * calculate( a, b -1)
    
# print(calculate(3, 4))


# Define a function named power that calculates the result of 'a' raised to the power of 'b'
def power(a, b):
    # Check if 'b' is 0 (base case for power function)
    if b == 0:
        # If 'b' is 0, return 1 (any number raised to the power of 0 is 1)
        return 1
    # Check if 'a' is 0 (base case for power function)
    elif a == 0:
        # If 'a' is 0, return 0 (0 raised to any power is 0)
        return 0
    # Check if 'b' is 1 (base case for power function)
    elif b == 1:
        # If 'b' is 1, return 'a' (any number raised to the power of 1 is the number itself)
        return a
    else:
        # If none of the base cases is met, recursively call the power function
        # to calculate 'a' multiplied by the result of 'a' raised to the power of 'b-1'
        return a * power(a, b - 1)

# Print the result of calling the power function with the input values 3 and 4
print(power(3, 4))


