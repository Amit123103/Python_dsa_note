# calculator creating

#default data type is str
# var1 = int(input("Enter first number: "))
# #var1 = int(var) # typecasting to int
# var2 = int(input("Enter second number: "))
# print("Sum:", var1 + var2)
# print("Difference:", var1 - var2)
# print("Product:", var1 * var2)
# print("Quotient:", var1 / var2)

# num1 = float(input("Enter first number: ")) # first data enter
# operator = input("Enter operator (+, -, *, /): ") # enter operator
# num2 = float(input("Enter second number: ")) # entering secong number

# if operator == "+":
#     print("Result =", num1 + num2)

# elif operator == "-":
#     print("Result =", num1 - num2)

# elif operator == "*":
#     print("Result =", num1 * num2)

# elif operator == "/":
#         print("Result =", num1 / num2)

# else:
#     print("Invalid operator")
# problem first  calculator using function. ---->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# def add(a, b):
#     return a + b
# def subtract(a, b):
#     return a - b
# def multiply(a, b):
#     return a * b
# def divide(a, b):
#     return a / b
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# print("1")
# print("2")
# print("3")
# print("4")
# choice = int(input("Enter your choice: "))
# if choice == 1:
#     print("Result =", add(num1, num2))
# elif choice == 2:
#     print("Result =", subtract(num1, num2))
# elif choice == 3:
#     print("Result =", multiply(num1, num2))
# elif choice == 4:
#     print("Result =", divide(num1, num2))
# else:
#     print("Invalid Choice")
 
 
#  #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<------------>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#  # 2nd Problem save output in list and a disctionary for the future use.
 # logic for this code
#     out_list = []
#     out_dict = {}
    # out_list.append(output)
    #key_1 = 0
    # out_dict[key_1] = output
    # key_1 = key_1 + 1

    
    

#simple while loop code

# i = 1
# while i <= 10:
#     print(i)
#     i  += 1
# second problem code for calculator with list and dictionary
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b
out_list = []
out_dict = {}
key = 0
while True:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        output = add(num1, num2)

    elif choice == 2:
        output = subtract(num1, num2)

    elif choice == 3:
        output = multiply(num1, num2)

    elif choice == 4:
        output = divide(num1, num2) 

    else:
        print("Invalid Choice")
        continue

    print("Result =", output)
    out_list.append(output)
    out_dict[key] = output
    key += 1

    print("All Results in List:")
    print(out_list)

    print("All Results in Dictionary:")
    print(out_dict)
