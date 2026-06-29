'''8. Handle division by zero using try and except.'''
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(a / b)
except ZeroDivisionError:
    print("Cannot divide by zero")

# def divide():
#     try:
#         a = int(input("Enter first number: "))
#         b = int(input("Enter second number: "))
#         print("Output :", a / b)
#     except ZeroDivisionError:
#         print("Cannot divide by zero")
# divide()