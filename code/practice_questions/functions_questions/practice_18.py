'''18. Execute a String Containing Python Code

Write a Python program to execute a string containing Python code.
'''
'''
code = """
a = 10
b = 20
print("Sum =", a + b)
"""

exec(code)
'''

# code = 'print("Hello World")'
# exec(code)
# Define a string variable 'mycode' containing a Python code as a string
mycode = 'print("hello world")'

# Define a multi-line string variable 'code' containing Python code as a string
code = """
def mutiply(x,y):
    return x*y

print('Multiply of 2 and 3 is: ',mutiply(2,3))
"""

# Execute the Python code represented by the string stored in the variable 'mycode'
exec(mycode)

# Execute the Python code represented by the multi-line string stored in the variable 'code'
exec(code) 

# expression = "100 + 200" 
# print(eval(expression))
'''eval() is a built-in Python function that evaluates a string as a Python expression and returns the resulting value. It can evaluate arithmetic, logical, and string expressions, but it cannot execute statements such as loops, assignments, or function definitions.
'''