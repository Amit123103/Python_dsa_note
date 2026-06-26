# two parshing loop creating one for string and second for Index to  read

# star_var = "hello"
# list_var = ['h','e','l','l','o']
# set_var ={1,2,3,4,5}
# print("Using the elements: ")
# for i in star_var:
#     print(i)
# print("Using the index: ")
#for i in range(len(list_var)):
     #print(list_var[i])
# for i in range(len(set_var)):
#     print(set_var[i])


'''1 concatination  joing + operator'''
# var = 'PYTHON'
# var1= 'ab'
# var_2 = var[2::]
# print(var_2)
# print(var1 + var_2)

'''Repeatition : repeating same object  multiple times using * operator '''

# var = 'python'
# a = (var + "\n" )* 5
# multi = '''this  
# is a
# multiline
# string'''

# print(multi)
# print(a) 
# print satements and  

# def my_function():
#     print("Hello")

# my_function()

# def function_name(a , b):
#     print(a+b)
#     return a +b
# function_name(2,3)

# creating fuction with two arguments default and keyword arguments

# default arguments

# def student(name , age = 18):
#     print(name, age)
# student("Amit")

# key word arguments
# def student(name, age):
#     print("Name:", name)
#     print("Age:", age)

# student(name="Amit", age=22)

# wild card  *args and *kywords
# def add(**a):
#     print(a)
# add(q=2, w=6,e=7, t=5)


# -----------------lambda function------------------------

# lambda function : A lambda function is a small anonymous function created using the lambda keyword. It can take any number of arguments but contains only one expression, and the result of that expression is returned automatically. 
# str1 = lambda **a : print(a)
# str1(q=2, w=6, e=7, t=5)

#### genrator function  
# yield  keyword  ------
# def demo():
#     yield 1

 # try , expect and finally
# try:
#     num = int(input("Enter Number: "))
#     print(10 / num)

# except ValueError:
#     print("Invalid Number")

# except ZeroDivisionError:
#     print("Cannot divide by zero")
    
# finally:
#     print("finally Block")
# file = open("file_name.txt", 'r')
# file.read()
# file.close()

# file = open("newfile.txt", "r                                                                                                                     ")
# #file.write("hello")
# print(file.read())
# #file.write("Hello")
# file.close()


'''OOps : object oriented Programming  '''
'''ORM: Operation Relationship mangement '''
'''1. Calculator Function

Write four separate functions:

add(a, b)
subtract(a, b)
multiply(a, b)
divide(a, b)

Take two numbers from the user and call the appropriate function based on the user's choice.

Concepts Covered:

Functions
Parameters
Return values
2. Even or Odd

Create a function is_even(num) that returns:

"Even" if the number is even
"Odd" otherwise

Call the function for a user-input number.

Concepts Covered:

Functions
Conditional statements
Return statement
3. Factorial Using Function

Create a function factorial(n) that returns the factorial of a number.

Example:

Input: 5
Output: 120

Concepts Covered:

Loops
Functions
4. Student Grade Function

Create a function calculate_grade(marks).

Rules:

90+ → A
75–89 → B
60–74 → C
Below 60 → Fail

Take marks as input and print the returned grade.

Concepts Covered:

Functions
if-elif ladder
OOP (5–9)
5. Student Class

Create a class Student.

Attributes:

name
age
course

Create a method display() that prints all student details.

Create two student objects.

Concepts Covered:

Class
Object
Constructor
Methods
6. Bank Account

Create a class BankAccount.

Attributes:

account_holder
balance

Methods:

deposit(amount)
withdraw(amount)
show_balance()

Withdrawal should only happen if sufficient balance exists.

Concepts Covered:

Objects
Instance variables
Methods
7. Rectangle Class

Create a class Rectangle.

Attributes:

length
breadth

Methods:

area()
perimeter()

Create an object and print both values.

Concepts Covered:

Classes
Methods
Formula implementation
8. Employee Salary

Create a class Employee.

Attributes:

name
salary

Method:

increment(percent)

Increase salary by the given percentage and display the updated salary.

Example:

Salary = 40000
Increment = 10%

Updated Salary = 44000

Concepts Covered:

Object manipulation
Updating instance variables
9. Inheritance Practice

Create a class Animal with method:

sound()

Create two child classes:

Dog
Cat

Override the sound() method.

Output:

Dog says Bark
Cat says Meow

Concepts Covered:

Inheritance
Method overriding
File Handling (10–12)
10. Create and Write File

Create a file named students.txt.

Take names of five students from the user and store them in the file.

After writing, display:

Data Saved Successfully

Concepts Covered:

open()
write()
close()
11. Read File

Read the contents of students.txt and display all student names.

Concepts Covered:

File reading
Loops
12. Count Lines

Read a text file and count:

Total lines
Total words

Display both counts.

Example:

Lines: 8
Words: 63

Concepts Covered:

File reading
String methods
Error Handling (13–15)
13. Safe Division

Take two numbers from the user.

Perform division using try-except.

If the denominator is zero, print:

Cannot divide by zero.

Concepts Covered:

try
except
ZeroDivisionError
14. Number Validation

Ask the user to enter an integer.

If the user enters text instead of a number, handle the error gracefully.

Example:

Input:
abc

Output:
Invalid input! Please enter a number.

Concepts Covered:

ValueError
Exception handling
15. File Not Found

Ask the user for a filename.

Try to open the file.

If the file does not exist, print:

File not found.

Otherwise, display its contents.

Concepts Covered:

File handling
FileNotFoundError
try-excep
'''
# 1. calculator Function    

# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def mul(a,b):
#     return a*b
# def div(a,b):
#     return a/b
 
# print(add(2,3))
# print(sub(2,3))
# print(mul(2,3))
# print(div(2,3))

# 2. Even or Odd
# def is_even(num):
#     if num % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"
# number = int(input("Enter a number: "))
# print(is_even(number))
# 3. creating factorial to retun 5 , 120
# def factorial(n):
#     a = 1
#     for i in range(1, n + 1):
#         a *= i
#     return a
# num = int(input("Enter a number: "))
# print("Factorial =", factorial(num))


#----------------

# 4. Student Grade Function

# def calculate_marks(marks):
#     if marks >= 90:
#         return "A"
#     elif marks >= 75:
#         return "B"
#     elif marks >= 60:
#         return "C"
#     else:
#         return "F"
# marks = int(input("Enter marks: "))
# print("Grade:", calculate_marks(marks))
 
 # 5. Student class
 
# class Student:
#     def __init__(self, name, age, course):
#         self.name = name
#         self.age = age
#         self.course = course
#     def display(self):
#         print("Name :", self.name)
#         print("Age :", self.age)
#         print("Course :", self.course)
# s1 = Student("Amit", 20, "DevOps")
# s2 = Student("Aditya", 21, "Machine learning")
# s1.display()
# print()
# s2.display()

# 6  bank account 
# class BankAccount:
#     def __init__(self, holder, balance):
#         self.account_holder = holder
#         self.balance = balance
#     def deposit(self, amount):
#         self.balance += amount
#         print("Amount Deposited Successfully")
#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print("Withdrawal Successful")
#         else:
#             print("Not Money Balance")
#     def show_balance(self):
#         print("Current Balance =", self.balance)
# obj = BankAccount("Amit", 5000)
# obj.deposit(2000)
# obj.withdraw(1000)
# obj.show_balance()

# 7. Rectangle Class
# class Rectangle:
#     def __init__(self, length, breadth):
#         self.length = length
#         self.breadth = breadth
#     def area(self):
#         return self.length * self.breadth
#     def meter(self):
#         return 2 * (self.length + self.breadth)
# r = Rectangle(10, 5)
# print("Area :", r.area())
# print("Perimeter :", r.meter())

#8. Employee Salary
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#     def increment(self, per):
#         increase = self.salary * per / 100
#         self.salary += increase
#         print("Updated Salary =", self.salary)
# name = Employee("Amit", 40000)
# name.increment(10)

# 9. Inheritance Practice
# class animal:
#     def sound(self):
#         print("animal makes a sound")
# class Dog(animal):
#     def sound(self):
#         print("Dog sound bark")
# class Cat(animal):
#     def sound(self):
#         print("Cat sound Meow")
# d = Dog()
# c = Cat()
# d.sound()
# c.sound()

# 10  Create and Write File

file = open("students.txt", "w")
for i in range(5):
    name = input("Enter student name: ")
    file.write(name + "\n")
file.close()
print("Data Saved Successfully")