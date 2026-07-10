'''7: Nested try-except Blocks

This example demonstrates how you can nest 'try-except' blocks to handle errors in different contexts. The division by zero is caught by the inner 'except', while the outer 'except' catches an index error, showing how to manage multiple potential exceptions in different parts of the code.
'''
try:
    # Outer try block
    try:
        # Attempt to divide by zero
        result = 10 / 0
    except ZeroDivisionError:
        # Handle division by zero
        print("Division by zero in inner try block.")
    # Attempt to access an invalid index
    my_list = [1, 2, 3]
    print(my_list[5])
except IndexError:
    # Handle the invalid index access in the outer try block
    print("Index out of range in outer try block.")
