'''1: Basic 'try-except' Block

In this example, the conversion of the string "100" to an integer succeeds, so the 'except' block is never executed. The 'try' block runs successfully, demonstrating a simple use case where no error occurs.
'''
try:
    # Attempt to convert a string to an integer, which will succeed
    number = int("100")
    print(f"Converted number: {number}")
except ValueError:
    # This block will not be executed since no exception occurs
    print("This will not print.")
