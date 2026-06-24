'''write a python program that accepts a string and calcualtes  the number of digit and letters

'''
# for loop using to create

# Accept a string from the user



str_vl = input("Enter a string: ")

letters = 0
digits = 0

for char in str_vl:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        digits += 1
    else:
        print("Invaild String")

print("Number of letters:", letters)
print("Number of digits:", digits)

# # while looop using to creating 

# str_vl = input("Enter a string: ")

# letters = 0
# digits = 0
# i = 0

# # for char in str_vl:
# while i < len(str_vl):    # len function provide us length of sequence
#     if str_vl[i].isalpha():
#         letters += 1
#     elif str_vl[i].isdigit():
#         digits += 1
# i += 1

# print("Number of letters:", letters)
# print("Number of digits:", digits)




# counter = 0
# Counter = len(str_vl)
# while Counter > 0:
#     print(str_vl[counter])
'''with keyword:
The with statement is used for resource management in Python.
It automatically handles setup and cleanup operations, such as opening and closing files,
making code safer, cleaner, and easier to read.
'''
with open('file_name.txt') as file:
    cont = file.read() 
    print(cont)
    
    
    
# global function 
# A namespace is a container that stores variable names and their values.

# Python mainly has:

# Built-in Namespace
# Global Namespace
# Local Namespace