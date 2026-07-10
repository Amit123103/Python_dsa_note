'''2: Handling an Exception with 'except'

Here, the string "Python" cannot be converted to an integer, so a 'ValueError' is raised and caught by the 'except' block. This prevents the program from crashing and allows you to handle the error gracefully.'''

try:
    # Attempt to convert an invalid string to an integer
    number = int("Python")
except ValueError:
    # This block handles the ValueError that occurs during conversion
    print("Invalid input! Cannot convert 'Python' to an integer.")
