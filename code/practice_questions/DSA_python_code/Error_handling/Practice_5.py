'''5: 'finally' Block

In this example, we attempt to open a non-existent file, raising a 'FileNotFoundError'. The 'finally' block executes regardless of the outcome, demonstrating its use for actions that should always be performed.
'''

try:
    # Attempt to open a file that doesn't exist
    file = open("test.txt", "r")
except FileNotFoundError:
    # Handle the exception if the file is not found
    print("File not found!")
finally:
    # This block always runs, whether an exception occurred or not
    print("This will always execute.")
