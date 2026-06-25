'''write a python program that accepts a string and calcualtes  the number of digit and letters

'''
# for loop using to create

# Accept a string from the user



# str_vl = input("Enter a string: ")

# letters = 0
# digits = 0

# for char in str_vl:
#     if char.isalpha():
#         letters += 1
#     elif char.isdigit():
#         digits += 1
#     else:
#         print("Invaild String")

# print("Number of letters:", letters)
# print("Number of digits:", digits)

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
# with open('file_name.txt') as file:
#     cont = file.read() 
#     print(cont)
    
    
    
# global function 
# A namespace is a container that stores variable names and their values.

# Python mainly has:

# Built-in Namespace
# Global Namespace
# Local Namespace


'''calander '''
# write a program to display the calender of the year entered by the user
# import calendar as cal

# year = int(input("Enter Year: "))

# print(cal.calendar(year))

# function that takes a list and retunrs a new list  with distinct elements form the first list

# def distinct_list(lst):
#     new_list = []
#     for item in lst:
#         if item not in new_list:
#             new_list.append(item)
#     return new_list
# numbers = [1,2,3,3,3,3,4,5]

# result = distinct_list(numbers)

# print("Ori_List:", numbers)
# print("Dist_List:", result)



# sample_list = [1, 2, 3, 3, 3, 3, 4, 5]

# new_list = []

# for i in sample_list:
#     if i not in new_list:
#         new_list.append(i)

# print("unique_List:", sample_list)
# print("Distinct_List:", new_list)


'''9. function that takes a number as a parameter and checks whether the number is prime  or not'''

# num = int(input("Enter a Number: "))

# count = 0

# for i in range(1, num + 1):
#     if num % i == 0:
#         count += 1

# if count == 2:
#     print("Prime Number")
# else:
#     print("Not a Prime Number")

# ----------------------------------------------------------------
'''
OOps : 
-- create file
-- logic to represent  laptop in code 
OOP Workflow

Problem
   ↓
Objects
   ↓
Attributes (Data)
   ↓
Methods (Behavior)
   ↓
Class
   ↓
Object
   ↓
Method Calls
'''
#  Cuurent object __ method 
# class Student:

#     def __init__(self, name, age):
#         self.name = name # name is class vaiable
#         self.age = age

#     def display(self):
#         print(self.name, self.age)

# s1 = Student("Amit", 22)
# s2 = Student("Rahul", 21)

# s1.display()
# s2.display()

# class Laptop:
#     model = "Apple"
#     def __init__(self, brand):
#         self.brand = brand
# obj = Laptop("HP")
# print(obj.model)
# print(obj.brand)


# class Student:
#     student = "AKm"
#     # def __init__(self, name):
#     #     self.name = name
        

# class Age:
#     Age = "21"
#     def __init__(self, age):
#         self.age = age
        
# class Course:
#     course = "English"
#     def __init__(self, subject):
#         self.subject = subject
        
# # obj = Student("Amit")
# obj = Age("22")
# obj = Course("Computer")       
        
# print(obj.)


# create a class representing a circle > Include methods to calculate its area and perimeter.
#
# class Area:
#     circle = ""
#     def __init__(self, circle):
#         self.circle = circle

