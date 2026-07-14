'''Sum Items in List

Write a Python program to sum all the items in a list.'''

# Define a function called sum_list that takes a list 'items' as input
def sum_list(items):
    # Initialize a variable 'sum_numbers' to store the sum of the numbers
    sum_numbers = 0
    # Iterate through each element 'x' in the input list 'items'
    for x in items:
        # Add the current element 'x' to the 'sum_numbers' variable
        sum_numbers += x
    # Return the final sum of the numbers
    return sum_numbers

# Call the sum_list function with the list [1, 2, -8] as input and print the result
print(sum_list([1, 2, -8]))
