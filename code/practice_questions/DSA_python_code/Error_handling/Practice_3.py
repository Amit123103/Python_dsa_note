''' 3: Using Multiple 'except' Blocks

This example demonstrates handling different exceptions separately. The 'ZeroDivisionError' is caught by the appropriate 'except' block, while the ‘ValueError’ block is skipped since no conversion error occurs.
'''

try:
    # Attempt to divide a number by zero
    result = 100 / 0
except ZeroDivisionError:
    # Handle division by zero
    print("Cannot divide by zero!")
except ValueError:
    # Handle conversion errors (this block won't run in this case)
    print("Conversion error occurred.")
