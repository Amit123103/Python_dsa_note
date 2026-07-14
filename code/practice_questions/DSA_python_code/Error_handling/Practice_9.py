'''Raising a 'ValueError' for Invalid InputScripting Languages

This example raises a ValueError if the function calculate_square_root receives a negative input, which is not valid for calculating a square root. This ensures that the function only processes valid inputs and provides clear error messaging when it doesn't.
'''
def calculate_square_root(x):
    # Check if the input is negative
    if x < 0:
        # Raise a ValueError for a negative input
        raise ValueError("Cannot calculate square root of a negative number.")
    return x ** 0.5

try:
    # Attempt to calculate the square root of -1, which will raise an exception
    result = calculate_square_root(-1)
except ValueError as e:
    # Handle the exception and print the error message
    print(f"Error: {e}")
