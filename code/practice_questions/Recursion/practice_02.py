'''Sum of List Using Recursion
Write a Python program to calculate the sum of a list of numbers using recursion.
'''
# def sum_list(num_list):
#     if len(num_list) == 1:
#         return num_list[0]
#     else:
#         return num_list[0] + sum_list(num_list[1:])
    
# print(sum_list([2,6,8,10,12]))


# Define a function named list_sum that takes a list of numbers as input
def list_sum(num_List):
    # Check if the length of the input list is 1
    if len(num_List) == 1:
        # If the list has only one element, return that element
        return num_List[0]
    else:
        # If the list has more than one element, return the sum of the first element
        # and the result of recursively calling the list_sum function on the rest of the list
        return num_List[0] + list_sum(num_List[1:])

# Print the result of calling the list_sum function with the input [2, 4, 5, 6, 7]
print(list_sum([2, 4, 5, 6, 7]))
