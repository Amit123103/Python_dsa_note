'''Raising a Built-in Exception

In this example, the 'divide_numbers' function checks if the denominator is zero before performing division. If it is, a 'ZeroDivisionError' is raised, preventing the division and signaling the error. The exception is then caught and handled, demonstrating how to use 'raise' for input validation.
'''

def divide_numbers(a, b):
    # Check if the denominator is zero
    if b == 0:
        # Raise a ZeroDivisionError if the denominator is zero
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

try:
    # Attempt to divide 10 by 0, which will raise an exception
    result = divide_numbers(100, 0)
except ZeroDivisionError as e:
    # Handle the exception and print the error message
    print(f"Error: {e}")
