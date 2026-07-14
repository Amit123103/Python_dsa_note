'''Harmonic Series Sum Using Recursion

Write a Python program to calculate the sum of harmonic series upto n terms.

Note: The harmonic sum is the sum of reciprocals of the positive integers.
Example :

harmonic series

1+ 1/2+1/3+1/4+1/5+ .....
'''
# def harmonic(num):
#     if num > 2:
#         return 1
#     else:
#         return 1 / num + harmonic(num-1)
# print(harmonic(7))



# Define a function named harmonic_sum that calculates the harmonic sum up to 'n' terms
def harmonic_sum(n):
    # Check if 'n' is less than 2 (base case for the harmonic sum)
    if n < 2:
        # If 'n' is less than 2, return 1 (base case value for the harmonic sum)
        return 1
    else:
        # If 'n' is greater than or equal to 2, calculate the reciprocal of 'n'
        # and add it to the result of recursively calling the harmonic_sum function with 'n - 1'
        return 1 / n + harmonic_sum(n - 1)

# Print the result of calling the harmonic_sum function with the input value 7
print(harmonic_sum(7))

# Print the result of calling the harmonic_sum function with the input value 4
print(harmonic_sum(4))
