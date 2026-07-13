'''
# 1. Normal Arguments
def adf(arg1, arg2):
    # Must pass exactly 2 positional arguments
    pass


# 2. *args
def adf(*args):
    # Can pass any number of positional arguments
    # Stored as a tuple
    pass


# 3. **kwargs
def adf(**kwargs):
    # Can pass any number of keyword arguments
    # Stored as a dictionary
    pass


# default : asdf( 8, 9)
# keyword : asdf(args1 = 9, args2 = 10)


| Call                     | Type                | How Python Matches                             |
| ------------------------ | ------------------- | ---------------------------------------------- |
| `asdf(8, 9)`             | Positional argument | By **position** (1st → `args1`, 2nd → `args2`) |
| `asdf(args1=8, args2=9)` | Keyword argument    | By **parameter name**                          |
| `asdf(args2=9, args1=8)` | Keyword argument    | By **parameter name**, so order doesn't matter |
'''

# delwte file 
# import os

# path = "Files/data.txt"

# if os.path.exists(path):
#     os.remove(path)
#     print("File Deleted")
# else:
#     print("File Not Found")

'''   Raise: Used to explicitly throw our own exception.
Assert: Used to test conditions during debugging; if the condition is false, execution stops with AssertionError.
Try-Except-Finally: Mechanism to handle runtime errors and ensure cleanup code always executes.
'''