'''2. Function Lambda Generator

Write a Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number. Scripting Languages

Sample Output:
Double the number of 15 = 30
Triple the number of 15 = 45
Quadruple the number of 15 = 60
Quintuple the number 15 = 75
'''
# def multiplier(n):
#     return lambda x: x * n


# double = multiplier(2)
# triple = multiplier(3)
# quadruple = multiplier(4)
# quintuple = multiplier(5)

# print("Double the number of 15 =", double(15))
# print("Triple the number of 15 =", triple(15))
# print("Quadruple the number of 15 =", quadruple(15))
# print("Quintuple the number of 15 =", quintuple(15))

# Define a function 'func_compute' that takes a parameter 'n' and returns a lambda function
# The returned lambda function multiplies its argument 'x' by 'n'
def func_compute(n):
    return lambda x: x * n

# Assign the result of calling func_compute with argument 2 to the variable 'result'
result = func_compute(2)
# Print the result of calling the lambda function stored in 'result' with argument 15
print("Double the number of 15 =", result(15))

# Reassign 'result' with the result of calling func_compute with argument 3
result = func_compute(3)
# Print the result of calling the lambda function stored in 'result' with argument 15
print("Triple the number of 15 =", result(15))

# Reassign 'result' with the result of calling func_compute with argument 4
result = func_compute(4)
# Print the result of calling the lambda function stored in 'result' with argument 15
print("Quadruple the number of 15 =", result(15))

# Reassign 'result' with the result of calling func_compute with argument 5
result = func_compute(5)
# Print the result of calling the lambda function stored in 'result' with argument 15
print("Quintuple the number 15 =", result(15))
