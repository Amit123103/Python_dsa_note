'''1. Lambda Add & Multiply

Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, also create a lambda function that multiplies argument x with argument y and prints the result.

Sample Output:
25
48
'''
# # Lambda function to add 15
# add_15 = lambda x: x + 15

# # Lambda function to multiply two numbers
# multiply = lambda x, y: x * y

# print(add_15(10))
# print(multiply(6, 8))

# Define a lambda function 'r' that takes a single argument 'a' and returns 'a + 15'
r = lambda a: a + 15

# Print the result of calling the lambda function 'r' with argument 10
print(r(10))

# Reassign 'r' to a new lambda function that takes two arguments 'x' and 'y' and returns their product
r = lambda x, y: x * y

# Print the result of calling the updated lambda function 'r' with arguments 12 and 4
print(r(12, 4))
