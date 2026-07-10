'''4: 'else' Block

In this example, the division operation is successful, so the 'else' block runs, printing the result. The 'else' block allows you to execute code only when the 'try' block doesn't raise any exceptions.
'''

try:
    # Attempt to divide two numbers
    result = 100 / 2
except ZeroDivisionError:
    # Handle division by zero
    print("Cannot divide by zero!")
else:
    # This block runs only if no exception occurs
    print(f"Division successful: {result}")
