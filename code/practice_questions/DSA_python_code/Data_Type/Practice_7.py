''' Multiply Items in List

Write a Python program to multiply all the items in a list.'''

# Define a function called multiply_list that takes a list 'items' as input
def multiply_list(items):
    # Initialize a variable 'tot' to store the product of the numbers, starting with 1
    tot = 1
    # Iterate through each element 'x' in the input list 'items'
    for x in items:
        # Multiply the current element 'x' with the 'tot' variable
        tot *= x
    # Return the final product of the numbers
    return tot

# Call the multiply_list function with the list [1, 2, -8] as input and print the result
print(multiply_list([1, 2, -8]))
