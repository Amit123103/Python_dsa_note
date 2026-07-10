'''Get Largest Number in List

Write a Python program to get the largest number from a list.'''

# Define a function called max_num_in_list that takes a list 'list' as input
def max_num_in_list(list):
    # Initialize a variable 'max' with the first element of the input list as the initial maximum
    max = list[0]
    # Iterate through each element 'a' in the input list 'list'
    for a in list:
        # Check if the current element 'a' is greater than the current maximum 'max'
        if a > max:
            # If 'a' is greater, update the maximum 'max' to 'a'
            max = a
    # Return the final maximum value in the list
    return max

# Call the max_num_in_list function with the list [1, 2, -8, 0] as input and print the result
print(max_num_in_list([1, 2, -8, 0]))
