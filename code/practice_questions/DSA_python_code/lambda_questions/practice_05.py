'''5. Integer Filter Lambda

Write a Python program to filter a list of integers using Lambda.

Original list of integers:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Even numbers from the said list:
[2, 4, 6, 8, 10]
Odd numbers from the said list:
[1, 3, 5, 7, 9] '''

# Create a list of integers named 'nums'
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Display a message indicating that the following output will show the original list of integers
print("Original list of integers:")
print(nums)

# Display a message indicating that the following output will show even numbers from the list
print("\nEven numbers from the said list:")

# Use the 'filter()' function with a lambda function to filter even numbers from 'nums'
# Create a new list 'even_nums' containing only the even numbers from the original list
even_nums = list(filter(lambda x: x % 2 == 0, nums))
print(even_nums)

# Display a message indicating that the following output will show odd numbers from the list
print("\nOdd numbers from the said list:")

# Use the 'filter()' function with a lambda function to filter odd numbers from 'nums'
# Create a new list 'odd_nums' containing only the odd numbers from the original list
odd_nums = list(filter(lambda x: x % 2 != 0, nums))
print(odd_nums) 







# list1= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print("Original list: ")
# print(list)
# filter_even = list(filter(lambda x:x%2==0,list1))
# print("\n Even no. : ")
# print(filter_even)

# filter_list = list(filter(lambda x:x %2 != 0, list1))
# print("\n odd number: ")
# print(filter_list)
